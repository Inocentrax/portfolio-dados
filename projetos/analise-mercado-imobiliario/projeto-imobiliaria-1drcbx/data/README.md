# Dados de entrada

O notebook original usa as entradas abaixo. Os datasets externos não foram copiados automaticamente.

```python
url = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv"
pd.read_csv(url)
dados = pd.read_csv(url, sep=";")
url ='https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
analise_imobiliaria = pd.read_csv(url, sep=";")
cop_dados = pd.read_csv(url, sep=";")
```

Se o caminho começa por /content ou MyDrive, ele pertence ao ambiente original. Obtenha o arquivo pela fonte do projeto, confirme permissão de uso e ajuste o caminho local antes de executar. Não envie dados pessoais ou credenciais ao repositório.

Registrar: fonte e link, data/versão, licença, unidade de observação e colunas obrigatórias.
