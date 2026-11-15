# Desempenho de alunos

Exemplo reproduzível de análise de notas, valores ausentes e regras simuladas de aprovação.

**Status:** Rascunho — origem dos dados e discussão final ainda pendentes.

[← Catálogo](../../../CATALOGO.md) · [Notebook](notebook.ipynb) · [Abrir no Colab](https://colab.research.google.com/github/Inocentrax/portfolio-dados/blob/main/em-andamento/desempenho-alunos/analise-alunos-1jgyrf/notebook.ipynb)

## O que foi organizado

- Amostra com nomes substituídos por identificadores.
- Caminhos relativos e orientação de upload no Colab.
- Estatísticas calculadas sobre notas observadas, sem preencher ausência com zero.
- Cenário de bônus separado da aprovação informada na base.
- Respostas calculadas pelo código, sem conclusões X/Y/Z.

## Dados e execução

Instale pandas, abra o notebook e execute em ordem. O CSV está em [data/raw](data/raw/amostra_estudo.csv); sua origem e os campos estão em [dados](data/README.md).

## Próximos passos

- [ ] Documentar origem e licença da amostra.
- [ ] Acrescentar visualizações e interpretar os limites.
- [ ] Confirmar a regra original de aprovação.

A base pequena serve para exercícios, não para generalizar desempenho de estudantes. O exemplo foi revisto a partir da versão anterior do projeto, preservada no histórico e no Drive.

## Verificação de execução

As células Python foram executadas sequencialmente em 15/11/2026, com Python 3.12.14, pandas 3.0.1 e NumPy 2.3.5 quando utilizados. Exemplos de erro didático estão tratados explicitamente. Isso verifica a execução do exemplo, sem certificar conclusões ou implementar as pendências.
