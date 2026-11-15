# Dados de entrada

O notebook original usa as entradas abaixo. Os datasets externos não foram copiados automaticamente.

```python
url = 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'#o padrão do sheets é 0, primeira pagina é emissoes_co2
dados_emissões = pd.read_excel(url)
percapita = pd.read_excel(url, sheet_name='emissoes_percapita')
fontes = pd.read_excel(url, sheet_name='fontes', usecols=[0,1,2,3])
fontes = pd.read_excel(url, sheet_name='fontes', usecols='A:D')
```

Se o caminho começa por /content ou MyDrive, ele pertence ao ambiente original. Obtenha o arquivo pela fonte do projeto, confirme permissão de uso e ajuste o caminho local antes de executar. Não envie dados pessoais ou credenciais ao repositório.

Registrar: fonte e link, data/versão, licença, unidade de observação e colunas obrigatórias.
