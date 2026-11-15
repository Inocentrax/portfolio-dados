# VGSales — origem e dicionário

## Arquivo conferido

- [Arquivo enviado no Drive](https://drive.google.com/file/d/1_AzIsBoF05i8-Kxxiwvssnu5O9_PB31e/view).
- 1.355.781 bytes; 16.598 registros e 11 colunas.
- MD5: 67fa6f5efdc100db4586aa80556e8620.
- SHA-256: e2076095ffcae2a92dbc6de6ecbd54455ee034bb38da550b2dc385e9265d4ebe.

O MD5 coincide com o publicado no [registro Zenodo atribuído a Gregory Smith](https://zenodo.org/records/5898311). A cópia pública está em [vgsales.csv](https://zenodo.org/records/5898311/files/vgsales.csv?download=1). Isso permite reproduzir o projeto sem liberar acesso ao seu Drive.

Referências de origem: [coleção no Kaggle](https://www.kaggle.com/datasets/gregorut/videogamesales), [registro arquivado e descrição](https://zenodo.org/records/5898311), [coletor do autor](https://github.com/GregorUT/vgchartzScrape), associado ao VGChartz. Não se presume que a licença do código coletor seja a mesma dos dados. A base integral não é republicada nesta pasta.

## Colunas

| Coluna | Significado |
|---|---|
| Rank | Ranking global do registro |
| Name | Nome do título |
| Platform | Plataforma do lançamento |
| Year | Ano de lançamento; pode estar ausente |
| Genre | Gênero |
| Publisher | Editora; pode estar ausente |
| NA_Sales | Vendas registradas na América do Norte, em milhões |
| EU_Sales | Vendas registradas na Europa, em milhões |
| JP_Sales | Vendas registradas no Japão, em milhões |
| Other_Sales | Vendas nas demais regiões, em milhões |
| Global_Sales | Total global na mesma escala |

Uma linha não identifica uma transação nem uma loja. PC não equivale a Steam. A descrição do arquivo informa ano de lançamento, não ano de venda.

## Executar

O código procura uma cópia em data_cache/vgsales.csv ou vgsales.csv na pasta do projeto. Se não houver, baixa a versão arquivada. O SHA-256 precisa coincidir com o acima; versões diferentes exigem revisão explícita. O cache fica fora do Git pelo gitignore.
