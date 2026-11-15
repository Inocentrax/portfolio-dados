# Dados de entrada

O notebook original usa as entradas abaixo. Os datasets externos não foram copiados automaticamente.

```python
url = "https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/superstore_data.csv"
dados = pd.read_csv(url)
dados2 = pd.read_csv(url2,sep=";")
dados_selecao = pd.read_csv(url, usecols=['Id','Year_Birth','Income'])
dados_selecao2 = pd.read_csv(url, usecols=[0,1,4])
```

Se o caminho começa por /content ou MyDrive, ele pertence ao ambiente original. Obtenha o arquivo pela fonte do projeto, confirme permissão de uso e ajuste o caminho local antes de executar. Não envie dados pessoais ou credenciais ao repositório.

Registrar: fonte e link, data/versão, licença, unidade de observação e colunas obrigatórias.
