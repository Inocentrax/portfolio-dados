"""Análise exploratória de anúncios de aluguel, com filtros e perda de dados explícitos."""
# %% Ambiente e obtenção dos dados
from pathlib import Path
from urllib.request import urlopen, Request
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
SOURCE_URL = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/1c1b10f2ea11e6e8b0826ac70e254660d248eba3/base-de-dados/aluguel.csv'
EXPECTED_SHA256 = '49a9840ce71dc55d6609f6c8938800cd3a0ea481a877013daf18c4b727bbca13'
cache_file = CACHE / 'aluguel-1c1b10f2.csv'
if not cache_file.exists():
    with urlopen(Request(SOURCE_URL, headers={'User-Agent': 'portfolio-dados'}), timeout=60) as response:
        cache_file.write_bytes(response.read())
raw_bytes = cache_file.read_bytes()
data_hash = hashlib.sha256(raw_bytes).hexdigest()
assert data_hash == EXPECTED_SHA256, 'O conteúdo difere da versão verificada; conferir fonte e arquivo em cache.'
raw = pd.read_csv(cache_file, sep=';')
required = {'Tipo', 'Bairro', 'Quartos', 'Vagas', 'Suites', 'Area', 'Valor', 'Condominio', 'IPTU'}
assert required.issubset(raw.columns), 'A estrutura do arquivo mudou; conferir a fonte.'

# %% Qualidade dos dados e recorte da análise
missing = raw.isna().sum()
missing.to_csv(BASE_DIR / 'dados-ausentes.csv', header=['quantidade'])
apartments = raw.loc[raw['Tipo'].eq('Apartamento')].copy()
valid = apartments.loc[apartments['Valor'].gt(0) & apartments['Area'].gt(0)].copy()
valid['aluguel_por_m2'] = valid['Valor'] / valid['Area']
# Ausência de condomínio não significa custo zero; manter o total desconhecido.
valid['aluguel_mais_condominio'] = valid['Valor'] + valid['Condominio']
neighborhoods = valid.groupby('Bairro').agg(anuncios=('Valor', 'size'), aluguel_mediano=('Valor', 'median'), area_mediana=('Area', 'median'), aluguel_mediano_m2=('aluguel_por_m2', 'median'))
ranked = neighborhoods.loc[neighborhoods['anuncios'].ge(30)].sort_values('aluguel_mediano', ascending=False)
ranked.to_csv(BASE_DIR / 'bairros-resumo.csv', index_label='bairro')
assert len(valid) <= len(apartments) <= len(raw)
assert valid['Valor'].gt(0).all() and valid['Area'].gt(0).all()

# %% Visualização dos bairros com suporte mínimo
top = ranked.head(10).sort_values('aluguel_mediano')
fig, ax = plt.subplots(figsize=(9, 5.5))
ax.barh(top.index, top['aluguel_mediano'], color='#1864ab')
ax.set(title='Apartamento: aluguel mediano por bairro', xlabel='Valor de aluguel anunciado (R$)', ylabel='')
ax.text(0, -0.15, 'Somente bairros com pelo menos 30 anúncios válidos; sem condomínio ou IPTU.', transform=ax.transAxes, fontsize=8)
ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
fig.savefig(ASSETS / 'aluguel-por-bairro.png', dpi=170, bbox_inches='tight')
plt.close(fig)

# %% Distribuição de valores e composição da base
p99 = valid['Valor'].quantile(0.99)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
axes[0].hist(valid.loc[valid['Valor'].le(p99), 'Valor'], bins=35, color='#0ca678', edgecolor='white')
axes[0].set(title='Distribuição de aluguéis de apartamentos', xlabel='Aluguel anunciado (R$)', ylabel='Anúncios')
axes[0].text(0, -0.22, 'Visualização até o percentil 99; estatísticas usam todos os valores válidos.', transform=axes[0].transAxes, fontsize=7)
types = raw['Tipo'].value_counts().head(7).sort_values()
axes[1].barh(types.index, types.values, color='#1864ab')
axes[1].set(title='Tipos mais frequentes na base original', xlabel='Anúncios')
for ax in axes:
    ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
fig.savefig(ASSETS / 'distribuicao-anuncios.png', dpi=170, bbox_inches='tight')
plt.close(fig)

# %% Respostas e rastreabilidade
summary = {
    'source_url': SOURCE_URL, 'dataset_sha256': data_hash,
    'original_rows': len(raw), 'apartment_rows': len(apartments), 'valid_apartments': len(valid),
    'excluded_apartments': len(apartments) - len(valid),
    'missing_by_column': {k: int(v) for k, v in missing.items()},
    'median_rent': float(valid['Valor'].median()), 'mean_rent': float(valid['Valor'].mean()),
    'median_rent_per_m2': float(valid['aluguel_por_m2'].median()),
    'neighborhoods_with_30_ads': len(ranked),
    'top_neighborhoods_by_median': [{'bairro': str(k), 'anuncios': int(v['anuncios']), 'aluguel_mediano': float(v['aluguel_mediano'])} for k, v in ranked.head(5).iterrows()],
    'known_rent_plus_condo_rows': int(valid['aluguel_mais_condominio'].notna().sum()),
    'environment': {'python': platform.python_version(), 'pandas': pd.__version__, 'numpy': np.__version__, 'matplotlib': matplotlib.__version__},
    'limitations': ['Anúncios não são contratos fechados ou imóveis únicos.', 'Período e representatividade devem ser confirmados na fonte.', 'Comparação por bairro sem controlar área, quartos ou localização fina.', 'Não é um modelo de precificação nem recomendação de investimento.'],
}
(BASE_DIR / 'resultados.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: summary[k] for k in ['original_rows', 'valid_apartments', 'median_rent', 'median_rent_per_m2']}, ensure_ascii=False, indent=2))
print('Resultados, tabelas e figuras gravados na pasta do projeto.')
