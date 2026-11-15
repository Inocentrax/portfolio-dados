"""Análise descritiva de vendas de videogames no snapshot VGSales enviado."""
# %% Ambiente e versão dos dados
from pathlib import Path
from urllib.request import Request, urlopen
import hashlib
import json
import platform
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
ASSETS = BASE_DIR / 'assets'
CACHE = BASE_DIR / 'data_cache'
ASSETS.mkdir(exist_ok=True)
CACHE.mkdir(exist_ok=True)
SOURCE_URL = 'https://zenodo.org/records/5898311/files/vgsales.csv?download=1'
EXPECTED_SHA256 = 'e2076095ffcae2a92dbc6de6ecbd54455ee034bb38da550b2dc385e9265d4ebe'
cache_file = CACHE / 'vgsales.csv'
if not cache_file.exists():
    uploaded = BASE_DIR / 'vgsales.csv'
    if uploaded.exists():
        cache_file.write_bytes(uploaded.read_bytes())
    else:
        with urlopen(Request(SOURCE_URL, headers={'User-Agent': 'portfolio-dados'}), timeout=90) as response:
            cache_file.write_bytes(response.read())
raw_bytes = cache_file.read_bytes()
data_hash = hashlib.sha256(raw_bytes).hexdigest()
assert data_hash == EXPECTED_SHA256, 'Versão diferente da base validada: conferir arquivo e fonte.'
raw = pd.read_csv(cache_file)
expected_columns = ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
assert list(raw.columns) == expected_columns
assert raw.shape == (16598, 11)

# %% Qualidade e regras de uso dos registros
missing = raw.isna().sum()
sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
for column in sales_columns:
    assert pd.api.types.is_numeric_dtype(raw[column])
    assert raw[column].notna().all() and raw[column].ge(0).all()
assert not raw.duplicated().any(), 'Conferir linhas idênticas antes de agregar.'
dados = raw.copy()
dados['Publisher'] = dados['Publisher'].fillna('Não informada')
dados['Year'] = pd.to_numeric(dados['Year'], errors='coerce').astype('Int64')
known_year = dados.dropna(subset=['Year']).copy()
regional_sum = dados[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum(axis=1)
regional_difference = dados['Global_Sales'] - regional_sum
quality = pd.DataFrame({'ausentes': missing, 'percentual': missing / len(raw) * 100})
quality.to_csv(BASE_DIR / 'qualidade-dados.csv', index_label='coluna')

# %% Plataformas, editoras, títulos e ano de lançamento
platforms = dados.groupby('Platform').agg(registros=('Name', 'size'), titulos_por_nome=('Name', 'nunique'), vendas_globais_milhoes=('Global_Sales', 'sum')).sort_values('vendas_globais_milhoes', ascending=False)
publishers = dados.groupby('Publisher').agg(registros=('Name', 'size'), titulos_por_nome=('Name', 'nunique'), vendas_globais_milhoes=('Global_Sales', 'sum')).sort_values('vendas_globais_milhoes', ascending=False)
games = dados.groupby('Name').agg(plataformas=('Platform', 'nunique'), registros=('Name', 'size'), vendas_globais_milhoes=('Global_Sales', 'sum')).sort_values('vendas_globais_milhoes', ascending=False)
cohorts = known_year.groupby('Year').agg(registros=('Name', 'size'), vendas_globais_milhoes=('Global_Sales', 'sum')).sort_index()
regions = dados[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
genres = dados.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
genre_shares = genres.div(genres.sum(axis=0), axis=1) * 100
for name, table in [('plataformas', platforms), ('editoras', publishers), ('titulos', games), ('coortes-lancamento', cohorts), ('generos-regioes-percentual', genre_shares)]:
    table.to_csv(BASE_DIR / f'{name}.csv')
assert np.isclose(platforms['vendas_globais_milhoes'].sum(), dados['Global_Sales'].sum())
assert np.isclose(publishers['vendas_globais_milhoes'].sum(), dados['Global_Sales'].sum())
assert np.allclose(genre_shares.sum(axis=0), 100)

# %% Principais plataformas e editoras
fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
for ax, table, title, color in [
    (axes[0], platforms, 'Plataformas', '#1864ab'),
    (axes[1], publishers, 'Editoras', '#0ca678'),
]:
    top = table.head(8).sort_values('vendas_globais_milhoes')
    ax.barh(top.index, top['vendas_globais_milhoes'], color=color)
    ax.set(title=title, xlabel='Vendas globais registradas (milhões de cópias)')
    ax.spines[['top', 'right']].set_visible(False)
fig.suptitle('VGSales — líderes de vendas no arquivo histórico', fontsize=14)
fig.tight_layout()
fig.savefig(ASSETS / 'plataformas-editoras.png', dpi=170, bbox_inches='tight')
plt.close(fig)

# %% Lançamentos e vendas acumuladas das coortes
fig, axes = plt.subplots(2, 1, figsize=(10, 6.5), sharex=True)
axes[0].bar(cohorts.index.to_numpy(dtype=int), cohorts['registros'], color='#1864ab')
axes[0].set(title='Registros agrupados por ano de lançamento', ylabel='Registros')
axes[1].plot(cohorts.index.to_numpy(dtype=int), cohorts['vendas_globais_milhoes'], color='#0ca678', marker='o', markersize=3)
axes[1].set(title='Vendas acumuladas registradas dos jogos de cada coorte', xlabel='Ano de lançamento', ylabel='Milhões de cópias')
for ax in axes:
    ax.spines[['top', 'right']].set_visible(False)
fig.text(0.08, 0.005, 'Year é ano de lançamento. A curva não representa vendas realizadas em cada ano-calendário.', fontsize=8)
fig.tight_layout(rect=(0, 0.035, 1, 1))
fig.savefig(ASSETS / 'coortes-lancamento.png', dpi=170, bbox_inches='tight')
plt.close(fig)

# %% Composição de gêneros em cada região
fig, ax = plt.subplots(figsize=(8, 6))
matrix = genre_shares.sort_index()
im = ax.imshow(matrix.values, cmap='Blues', aspect='auto', vmin=0, vmax=matrix.values.max())
ax.set(xticks=np.arange(4), xticklabels=['Am. do Norte', 'Europa', 'Japão', 'Outras'], yticks=np.arange(len(matrix)), yticklabels=matrix.index, title='Participação de cada gênero nas vendas da região')
for row in range(len(matrix)):
    for col in range(4):
        value = matrix.iloc[row, col]
        ax.text(col, row, f'{value:.1f}%', ha='center', va='center', fontsize=8, color='white' if value > matrix.values.max() * 0.55 else '#183153')
fig.colorbar(im, ax=ax, label='Participação na região (%)')
fig.tight_layout()
fig.savefig(ASSETS / 'generos-regioes.png', dpi=170, bbox_inches='tight')
plt.close(fig)

# %% Títulos com maiores totais e registro dos resultados
fig, ax = plt.subplots(figsize=(10, 5.5))
top_games = games.head(10).sort_values('vendas_globais_milhoes')
ax.barh(top_games.index, top_games['vendas_globais_milhoes'], color='#1864ab')
ax.set(title='Maiores totais por título, somando plataformas', xlabel='Vendas globais registradas (milhões de cópias)')
ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
fig.savefig(ASSETS / 'titulos.png', dpi=170, bbox_inches='tight')
plt.close(fig)
publisher_by_count = publishers.sort_values('registros', ascending=False)
peak = cohorts.sort_values('vendas_globais_milhoes', ascending=False).iloc[0]
peak_year = int(cohorts['vendas_globais_milhoes'].idxmax())
result = {
    'rows': len(raw), 'columns': list(raw.columns), 'dataset_sha256': data_hash,
    'dataset_md5': hashlib.md5(raw_bytes).hexdigest(), 'reference_doi': '10.5281/zenodo.5898311',
    'unit': 'milhões de cópias', 'row_meaning': 'registro de título/plataforma, não jogo único',
    'platforms': int(raw.Platform.nunique()), 'distinct_names': int(raw.Name.nunique()),
    'missing': {key: int(value) for key, value in missing.items()},
    'rows_removed_by_blanket_dropna': int(len(raw) - len(raw.dropna())),
    'rows_kept': len(dados), 'rows_used_for_release_year': len(known_year),
    'duplicate_full_rows': int(raw.duplicated().sum()),
    'global_sales_millions': float(raw.Global_Sales.sum()),
    'top_platform': {'name': str(platforms.index[0]), 'sales_millions': float(platforms.iloc[0]['vendas_globais_milhoes'])},
    'top_publisher_sales': {'name': str(publishers.index[0]), 'sales_millions': float(publishers.iloc[0]['vendas_globais_milhoes'])},
    'top_publisher_records': {'name': str(publisher_by_count.index[0]), 'records': int(publisher_by_count.iloc[0]['registros'])},
    'top_title': {'name': str(games.index[0]), 'sales_millions': float(games.iloc[0]['vendas_globais_milhoes'])},
    'largest_release_cohort': {'year': peak_year, 'sales_millions': float(peak['vendas_globais_milhoes'])},
    'regional_totals_millions': {k: float(v) for k, v in regions.items()},
    'max_abs_regional_vs_global_difference': float(regional_difference.abs().max()),
    'rows_regional_difference_above_0_05': int(regional_difference.abs().gt(0.05).sum()),
    'environment': {'python': platform.python_version(), 'pandas': pd.__version__, 'numpy': np.__version__, 'matplotlib': matplotlib.__version__},
    'limitations': ['Snapshot histórico; não é o mercado atual.', 'Sem identificação da loja de venda; não é uma base exclusiva da Steam.', 'Year é lançamento, não ano da venda.', 'Cobertura e estimativas da fonte não constituem um censo da indústria.', 'Agrupar Name pode reunir versões diferentes com o mesmo nome.'],
}
(BASE_DIR / 'resultados.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: result[k] for k in ['rows', 'rows_kept', 'missing', 'top_platform', 'top_publisher_sales', 'top_publisher_records', 'top_title', 'largest_release_cohort']}, ensure_ascii=False, indent=2))
print('Análise, tabelas e quatro gráficos concluídos.')
