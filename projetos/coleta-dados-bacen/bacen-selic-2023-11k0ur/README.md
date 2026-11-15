# bacen selic 2023

Coleta JSON da série SGS 11 para janeiro de 2023, leitura e persistência; sem explicação em Markdown.

**Status:** Em andamento. **Verificação:** revisão estática; execução completa pendente.

[← Catálogo](../../../CATALOGO.md) · [Notebook](notebook.ipynb) · [Abrir no Colab](https://colab.research.google.com/github/Inocentrax/portfolio-dados/blob/main/projetos/coleta-dados-bacen/bacen-selic-2023-11k0ur/notebook.ipynb)

## O que existe

16 células com código e 0 células de texto no arquivo de origem. O desenvolvimento está preservado em um notebook com abertura descritiva e seção de continuidade.

## Próximos passos

- [ ] Explicar série, unidade e intervalo (o nome sugere 2023 inteiro, mas a consulta é apenas janeiro).
- [ ] parametrizar datas, tratar falha HTTP e timeout, substituir caminho /content e tornar a gravação repetível (modo xb falha se o arquivo já existir).
- [ ] Acrescentar análise simples ou apresentá-lo como projeto de coleta.

## Executar

Abra o notebook no Colab pelo link acima ou em Jupyter/VS Code. As dependências diretas detectadas estão em requirements.txt; a combinação de versões ainda precisa ser verificada.

Consulte [dados de entrada](data/README.md). Arquivos em caminhos privados do Colab não acompanham automaticamente este projeto.

## Limites e origem

Este arquivo está identificado como **Em andamento**. A organização e a revisão estática não equivalem à validação completa da análise. Consulte as pendências antes de usar seus resultados.

A ausência de erros salvos não foi usada como prova de funcionamento.

Autoria e referências mencionadas nas células foram preservadas. O título original era **bacen_selic_2023.ipynb**. Alterações organizacionais: abertura descritiva, nomes de pastas estáveis, retirada de células vazias e metadados/outputs de sessão.
