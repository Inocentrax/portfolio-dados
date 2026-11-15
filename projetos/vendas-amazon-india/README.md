# Vendas da Amazon na Índia

Análise exploratória em Python de valores e quantidades por estado da Índia, com comparação regional e visualizações.

**Status:** Análise em revisão.

[← Catálogo de projetos e estudos](../../README.md)

---

Análise regional do arquivo `AmazonSaleReport.csv`, usando pandas, Matplotlib e Seaborn. O objetivo é comparar valores e quantidades por estado e explorar sua distribuição.

## Como executar

```bash
python -m pip install -r requirements.txt
python baixar_dados.py
python TrabalhoAmazonVendas.py
```

O comando `baixar_dados.py` obtém a versão da base preservada no repositório original, valida seu conteúdo e a salva nesta pasta. Depois disso, o CSV está na raiz e o script agora resolve o caminho a partir do próprio arquivo, sem depender de uma pasta particular no Windows. Os gráficos são abertos em janelas Matplotlib; use um ambiente com suporte gráfico.

## O que o código faz

1. Lê o CSV e prepara colunas, duplicatas e nulos.
2. Agrega o valor registrado em `Amount` por `ship-state`.
3. Compara os estados com maiores e menores totais.
4. Mostra distribuições, dispersões e gráficos ao longo do tempo.

## Mapa dos arquivos

- [TrabalhoAmazonVendas.py](TrabalhoAmazonVendas.py): preparação e visualizações.
- [baixar_dados.py](baixar_dados.py): obtém a base de 19 MB de uma versão fixa; o CSV baixado não é versionado novamente.
- [requirements.txt](requirements.txt): dependências declaradas.
- [Contexto original](docs/CONTEXTO_ORIGINAL.md): descrição histórica detalhada.

## Limitações e próximos passos

- [ ] Documentar fonte original, licença, período e unidade de cada linha.
- [ ] Medir o impacto de `dropna()` em todas as colunas e definir tratamento por campo.
- [ ] Definir como cancelamentos/devoluções entram nas agregações; total de `Amount` não é necessariamente receita líquida.
- [ ] Substituir conversões monetárias fixas por análise em INR ou taxa/data explicitamente documentadas. As taxas existentes são ilustrativas, não cotações atuais.
- [ ] Validar resultados e salvar figuras/indicadores para leitura sem executar o script.

Os gráficos descrevem a base; recomendações de investimento em marketing exigem evidências adicionais.

## Continuidade no portfólio

Esta pasta é a versão de referência para continuar o trabalho. O [repositório original](https://github.com/Inocentrax/Amazon-Vendas-India) conserva seu histórico anterior.

[Catálogo](../../CATALOGO.md) · [Próximos passos](../../PROXIMOS_PASSOS.md)
