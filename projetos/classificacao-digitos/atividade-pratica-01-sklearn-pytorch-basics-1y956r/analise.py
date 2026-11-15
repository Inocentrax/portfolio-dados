"""Experimento reproduzível: baseline, regressão logística e MLP no Digits."""
# %% Ambiente e reprodutibilidade
from pathlib import Path
import hashlib
import json
import random
import platform
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader

BASE_DIR = Path(__file__).resolve().parent
ASSETS = BASE_DIR / 'assets'
ASSETS.mkdir(exist_ok=True)
SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.set_num_threads(2)

# %% Dados e divisão estratificada
digits = load_digits()
X, y = digits.data, digits.target
indices = np.arange(len(y))
train_idx, test_idx = train_test_split(indices, test_size=0.2, stratify=y, random_state=SEED)
X_train, X_test = X[train_idx], X[test_idx]
y_train, y_test = y[train_idx], y[test_idx]
assert set(train_idx).isdisjoint(test_idx)
assert len(train_idx) + len(test_idx) == len(y)
scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# %% Baseline e regressão logística
baseline = DummyClassifier(strategy='most_frequent').fit(X_train_scaled, y_train)
logistic = LogisticRegression(max_iter=1000, random_state=SEED).fit(X_train_scaled, y_train)
predictions = {
    'Baseline': baseline.predict(X_test_scaled),
    'Logística': logistic.predict(X_test_scaled),
}

# %% MLP — 20 épocas definidas antes de olhar o teste
class DigitMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(nn.Linear(64, 64), nn.ReLU(), nn.Linear(64, 32), nn.ReLU(), nn.Linear(32, 10))

    def forward(self, x):
        return self.network(x)

model = DigitMLP()
train_dataset = TensorDataset(torch.tensor(X_train_scaled, dtype=torch.float32), torch.tensor(y_train, dtype=torch.long))
loader = DataLoader(train_dataset, batch_size=64, shuffle=True, generator=torch.Generator().manual_seed(SEED))
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()
loss_history = []
for epoch in range(20):
    model.train()
    loss_sum = 0.0
    for batch_x, batch_y in loader:
        optimizer.zero_grad()
        loss = criterion(model(batch_x), batch_y)
        loss.backward()
        optimizer.step()
        loss_sum += loss.item() * len(batch_x)
    loss_history.append(loss_sum / len(train_dataset))

model.eval()
with torch.no_grad():
    predictions['MLP'] = model(torch.tensor(X_test_scaled, dtype=torch.float32)).argmax(dim=1).numpy()

# %% Avaliação no teste reservado
metrics = {name: {'accuracy': float(accuracy_score(y_test, pred)), 'f1_macro': float(f1_score(y_test, pred, average='macro'))} for name, pred in predictions.items()}
for name, values in metrics.items():
    print(f"{name}: acurácia={values['accuracy']:.4f}; F1 macro={values['f1_macro']:.4f}")
fig, ax = plt.subplots(figsize=(8, 4.5))
names = list(metrics)
positions = np.arange(len(names))
ax.bar(positions - 0.18, [metrics[n]['accuracy'] for n in names], width=0.36, label='Acurácia', color='#1864ab')
ax.bar(positions + 0.18, [metrics[n]['f1_macro'] for n in names], width=0.36, label='F1 macro', color='#0ca678')
ax.set(xticks=positions, xticklabels=names, ylim=(0, 1.08), ylabel='Métrica no teste', title='Classificação de dígitos — 360 amostras de teste')
ax.legend(frameon=False)
ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
fig.savefig(ASSETS / 'comparacao-modelos.png', dpi=170)
plt.close(fig)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
for ax, name in zip(axes, ['Logística', 'MLP']):
    ConfusionMatrixDisplay(confusion_matrix(y_test, predictions[name], labels=np.arange(10))).plot(ax=ax, cmap='Blues', colorbar=False, values_format='d')
    ax.set_title(name)
    ax.set(xlabel='Classe prevista', ylabel='Classe verdadeira')
fig.tight_layout()
fig.savefig(ASSETS / 'matrizes-confusao.png', dpi=170)
plt.close(fig)

fig, ax = plt.subplots(figsize=(7, 3.5))
ax.plot(np.arange(1, 21), loss_history, color='#1864ab', marker='o', markersize=3)
ax.set(title='MLP — perda média no treinamento', xlabel='Época', ylabel='Entropia cruzada')
ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
fig.savefig(ASSETS / 'treinamento.png', dpi=170)
plt.close(fig)

# %% Registro do experimento
result = {
    'dataset': 'sklearn.datasets.load_digits',
    'rows': len(y), 'features': X.shape[1], 'train_rows': len(train_idx), 'test_rows': len(test_idx),
    'seed': SEED, 'epochs': 20, 'batch_size': 64, 'learning_rate': 0.001,
    'test_indices_sha256': hashlib.sha256(test_idx.astype('<i8').tobytes()).hexdigest(),
    'metrics_test': metrics,
    'loss_history': loss_history,
    'environment': {'python': platform.python_version(), 'numpy': np.__version__, 'scikit-learn': sklearn.__version__, 'torch': torch.__version__, 'matplotlib': matplotlib.__version__},
    'limitations': ['Uma única divisão estratificada.', 'Sem busca de hiperparâmetros ou intervalos de confiança.', 'Imagens 8x8 do Digits; não mede desempenho em imagens externas.'],
}
(BASE_DIR / 'resultados.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
assert np.isfinite(loss_history).all()
assert all(0 <= value <= 1 for item in metrics.values() for value in item.values())
print('Resultados e figuras gravados na pasta do projeto.')
