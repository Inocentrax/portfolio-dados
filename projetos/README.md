# Projetos em dados e aprendizado de máquina

[← Catálogo](../CATALOGO.md) · [Quadro](../QUADRO.md)

## Demonstrações concluídas

- [Classificação de dígitos](../projetos/classificacao-digitos/atividade-pratica-01-sklearn-pytorch-basics-1y956r/): execução e resultados verificados em 15/11/2026.
- [Anúncios de aluguel](../projetos/analise-mercado-imobiliario/projeto-imobiliaria-1drcbx/): execução e resultados verificados em 15/11/2026.

- [Vendas de videogames](../projetos/vendas-videogames/analise-games-1y8onn/): análise de plataformas, editoras, títulos e regiões.

## Em andamento

- [bacen selic 2023](../projetos/coleta-dados-bacen/bacen-selic-2023-11k0ur/): Explicar série, unidade e intervalo (o nome sugere 2023 inteiro, mas a consulta é apenas janeiro); parametrizar datas, tratar falha HTTP e timeout, substituir caminho /content e tornar a gravação repetível (modo xb falha se o arquivo já existir). Acrescentar análise simples ou apresentá-lo como projeto de coleta.
- [Estudo sobre SVC E LinearSvc](../projetos/estudos-machine-learning/estudo-sobre-svc-e-linearsvc-1b8yjj/): Documentar dados e créditos, transformar comparação em tabela com métricas e tempo, fixar ano de referência para idade do veículo (datetime.today muda o experimento), padronizar seeds e considerar pipeline.
- [Analise de Topicos em Emails](../projetos/topicos-emails/analise-de-topicos-em-emails-1badcb/): Preservar três autores; acrescentar import/dependência unidecode; padronizar ambiente e unificar com três variantes LDA; usar amostra sintética/anonimizada e revisar saídas para não expor e-mails. Relacionar rótulos aos tópicos efetivamente treinados.
- [Trabalho Aprendizado Não Supervisionado](../projetos/ideb-regiao-norte/trabalho-aprendizado-nao-supervisionado-1z1dwg/): Comparar com APRIORI para formar versão canônica; verificar etapas escolares da planilha versus colunas usadas, dados faltantes após conversão, escala dos radares e critérios dos clusters. Incluir fonte INEP, dicionário e limitações.
- [Projeto Steam Games](../projetos/analise-jogos-steam/projeto-steam-games-1jnxam/): Prioridade de portfólio após revisão: localizar fonte/licença/data do CSV, distinguir playtime de número de jogadores e owners de vendas; aplicar ranking antes de head(10) da CAPCOM; revisar moeda/centavos e escrever respostas verificadas às perguntas.
- [SENSORES GALPÕES](../projetos/sensores-industriais/sensores-galpoes-1uaygj/): Rotular dados como sintéticos, concluir regras de qualidade, tratar nulos e comparar antes/depois; distinguir Falha de Inativa (o dataset não tem status Inativa). Não apresentar como implantação industrial real.
- [vetorização comum](../projetos/classificacao-imagens/vetorizacao-comum-1gefv-/): Integrar com embeddings no mesmo projeto, adicionar imports pyplot/seaborn ausentes, corrigir explicação Z-score versus MinMax e salvar scaler junto do modelo. Documentar origem/divisão das imagens e sementes.
- [vetorização com embbedings](../projetos/classificacao-imagens/vetorizacao-com-embbedings-1o3kam/): Comparar com pixels na mesma divisão, documentar download/pesos e imagens, externalizar caminhos e salvar pipeline de transformação/modelo. Registrar custo e limitações.
- [APRIORI](../projetos/ideb-regiao-norte/apriori-1hg841/): Candidata a fonte junto do Trabalho Não Supervisionado. Separar exploração/modelagem/regras, remover instalação experimental do fluxo principal, corrigir URL em célula de código, distinguir anos iniciais/finais e município/escola; preservar anomalias por rede e município em colunas diferentes (hoje Anomalia é zerada). Validar tratamento de nulos antes de conclusões.
- [desafio ciia](../projetos/classificacao-tweets/desafio-ciia-1q-jic/): Criar validação estratificada antes de ajustar TF-IDF, reportar F1 e matriz de confusão fora do treino; preservar IDs e cardinalidade de test/submission, gerar arquivo de envio e documentar fonte/regras. Corrigir texto: stopwords efetivamente em inglês.

## Projetos integrados de outros repositórios

- [Vendas da Amazon na Índia](vendas-amazon-india/): Em andamento. Validar tratamento de nulos, cancelamentos e unidades monetárias; salvar resultados reproduzíveis.
- [Extinção animal — busca de espécies](extincao-animal/): Estudo. Revisar nomes, referências e estado de conservação; melhorar acessibilidade e pesquisa com acentos.
