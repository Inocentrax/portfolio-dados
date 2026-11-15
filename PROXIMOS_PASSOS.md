# Próximos passos

Use este arquivo para retomar o trabalho sem abrir vários Colabs. Cada entrada aponta para o notebook e sua lista específica de pendências.

## Entregas verificadas

- [Classificação de dígitos](projetos/classificacao-digitos/atividade-pratica-01-sklearn-pytorch-basics-1y956r/): experimento, métricas e gráficos publicados.
- [Anúncios de aluguel](projetos/analise-mercado-imobiliario/projeto-imobiliaria-1drcbx/): recorte, tabelas e figuras publicados.

[Quadro e tarefas](QUADRO.md) · [Bases encontradas no Drive](docs/BASES_NO_DRIVE.md)

- [Vendas de videogames](projetos/vendas-videogames/analise-games-1y8onn/): análise e dados conferidos, com quatro figuras.

## Ordem sugerida

1. Dígitos: evoluções opcionais após a demonstração já verificada.
2. Coleta Bacen: fechar execução; análise imobiliária já tem demonstração verificada.
3. Steam e classificação de imagens: revisar métricas e origem dos dados.
4. Tweets: avaliar fora do treino.
5. IDEB e tópicos de e-mails: consolidar pipeline e ambiente.
6. Desenvolver rascunhos conforme interesse, mantendo o status atualizado.

## Projetos e rascunhos

### [bacen selic 2023](projetos/coleta-dados-bacen/bacen-selic-2023-11k0ur/)

**Status:** Em andamento.

- [ ] Explicar série, unidade e intervalo (o nome sugere 2023 inteiro, mas a consulta é apenas janeiro); parametrizar datas, tratar falha HTTP e timeout, substituir caminho /content e tornar a gravação repetível (modo xb falha se o arquivo já existir). Acrescentar análise simples ou apresentá-lo como projeto de coleta.
- [ ] Registrar como reproduzir e os resultados verificados.


### [Estudo sobre SVC E LinearSvc](projetos/estudos-machine-learning/estudo-sobre-svc-e-linearsvc-1b8yjj/)

**Status:** Em andamento.

- [ ] Documentar dados e créditos, transformar comparação em tabela com métricas e tempo, fixar ano de referência para idade do veículo (datetime.today muda o experimento), padronizar seeds e considerar pipeline.
- [ ] Registrar como reproduzir e os resultados verificados.

### [Ideia de fluxo de processamento de linguagem](em-andamento/arquivo-revisao/ideia-de-fluxo-de-processamento-de-linguagem-18fstx/)

**Status:** Rascunho.

- [ ] Transformar em nota de arquitetura com objetivo e escopo ou manter como ideia. Não publicar como implementação.
- [ ] Registrar como reproduzir e os resultados verificados.

### [Projeto Cursos de Graduação](em-andamento/cursos-graduacao/projeto-cursos-de-graduacao-1ftx7d/)

**Status:** Rascunho.

- [ ] Localizar CSV e data de extração, formular pergunta geográfica adequada a categorias, criar agregações/gráficos por UF e concluir antes de promover a projeto.
- [ ] Registrar como reproduzir e os resultados verificados.


### [Analise de Topicos em Emails](projetos/topicos-emails/analise-de-topicos-em-emails-1badcb/)

**Status:** Em andamento.

- [ ] Preservar três autores; acrescentar import/dependência unidecode; padronizar ambiente e unificar com três variantes LDA; usar amostra sintética/anonimizada e revisar saídas para não expor e-mails. Relacionar rótulos aos tópicos efetivamente treinados.
- [ ] Registrar como reproduzir e os resultados verificados.

### [Trabalho Aprendizado Não Supervisionado](projetos/ideb-regiao-norte/trabalho-aprendizado-nao-supervisionado-1z1dwg/)

**Status:** Em andamento.

- [ ] Comparar com APRIORI para formar versão canônica; verificar etapas escolares da planilha versus colunas usadas, dados faltantes após conversão, escala dos radares e critérios dos clusters. Incluir fonte INEP, dicionário e limitações.
- [ ] Registrar como reproduzir e os resultados verificados.

### [Projeto Steam Games](projetos/analise-jogos-steam/projeto-steam-games-1jnxam/)

**Status:** Em andamento.

- [ ] Prioridade de portfólio após revisão: localizar fonte/licença/data do CSV, distinguir playtime de número de jogadores e owners de vendas; aplicar ranking antes de head(10) da CAPCOM; revisar moeda/centavos e escrever respostas verificadas às perguntas.
- [ ] Registrar como reproduzir e os resultados verificados.

### [SENSORES GALPÕES](projetos/sensores-industriais/sensores-galpoes-1uaygj/)

**Status:** Em andamento.

- [ ] Rotular dados como sintéticos, concluir regras de qualidade, tratar nulos e comparar antes/depois; distinguir Falha de Inativa (o dataset não tem status Inativa). Não apresentar como implantação industrial real.
- [ ] Registrar como reproduzir e os resultados verificados.

### [Analise alunos](em-andamento/desempenho-alunos/analise-alunos-1jgyrf/)

**Status:** Rascunho.

- [ ] Localizar ou criar dados sintéticos, restringir replace à coluna Notas, definir escala/regra de bônus e aprovação, corrigir import de pyplot e substituir todas as conclusões de exemplo por cálculos. Revisar identificação de alunos.
- [ ] Registrar como reproduzir e os resultados verificados.


### [Índice de preços ao produtor — preparação dos dados](em-andamento/ipp-ibge/indice-de-precos-ao-produtor-preparacao-dos-dados-1gw0aw/)

**Status:** Rascunho.

- [ ] Localizar JSON e fonte/tabela/período, tratar códigos vazios e marcadores de ausência antes de conversão; desenvolver séries/gráficos e respostas sobre setores/sazonalidade.
- [ ] Registrar como reproduzir e os resultados verificados.

### [Solos da Amazônia — exploração inicial](em-andamento/solos-amazonia/solos-da-amazonia-exploracao-inicial-1vzus2/)

**Status:** Rascunho.

- [ ] Definir pergunta espacial, recuperar origem/versão/CRS dos dados, validar dicionário contra colunas reais e concluir exploração antes de propor modelo.
- [ ] Registrar como reproduzir e os resultados verificados.

### [vetorização comum](projetos/classificacao-imagens/vetorizacao-comum-1gefv-/)

**Status:** Em andamento.

- [ ] Integrar com embeddings no mesmo projeto, adicionar imports pyplot/seaborn ausentes, corrigir explicação Z-score versus MinMax e salvar scaler junto do modelo. Documentar origem/divisão das imagens e sementes.
- [ ] Registrar como reproduzir e os resultados verificados.

### [vetorização com embbedings](projetos/classificacao-imagens/vetorizacao-com-embbedings-1o3kam/)

**Status:** Em andamento.

- [ ] Comparar com pixels na mesma divisão, documentar download/pesos e imagens, externalizar caminhos e salvar pipeline de transformação/modelo. Registrar custo e limitações.
- [ ] Registrar como reproduzir e os resultados verificados.

### [Atividade 1 Jairo AP SUPERVISIONADO](em-andamento/indicadores-diabetes/atividade-1-jairo-ap-supervisionado-1qdrbp/)

**Status:** Rascunho.

- [ ] Rever remoção de valores válidos nas colunas de dias; documentar dataset e critérios. Se desenvolver classificação, dividir antes de ajustes e aplicar reamostragem somente no treino; concluir métricas/limitações.
- [ ] Registrar como reproduzir e os resultados verificados.

### [APRIORI](projetos/ideb-regiao-norte/apriori-1hg841/)

**Status:** Em andamento.

- [ ] Candidata a fonte junto do Trabalho Não Supervisionado. Separar exploração/modelagem/regras, remover instalação experimental do fluxo principal, corrigir URL em célula de código, distinguir anos iniciais/finais e município/escola; preservar anomalias por rede e município em colunas diferentes (hoje Anomalia é zerada). Validar tratamento de nulos antes de conclusões.
- [ ] Registrar como reproduzir e os resultados verificados.

### [desafio ciia](projetos/classificacao-tweets/desafio-ciia-1q-jic/)

**Status:** Em andamento.

- [ ] Criar validação estratificada antes de ajustar TF-IDF, reportar F1 e matriz de confusão fora do treino; preservar IDs e cardinalidade de test/submission, gerar arquivo de envio e documentar fonte/regras. Corrigir texto: stopwords efetivamente em inglês.
- [ ] Registrar como reproduzir e os resultados verificados.

## Estudos

Os estudos têm tarefas específicas nos respectivos READMEs. Use o [catálogo](CATALOGO.md) para selecionar um assunto. Não é necessário concluir todos para desenvolver um projeto.

### [Vendas da Amazon na Índia](projetos/vendas-amazon-india/)

- [ ] Validar tratamento de nulos, cancelamentos e unidades monetárias; salvar resultados reproduzíveis.

### [Extinção animal — busca de espécies](projetos/extincao-animal/)

- [ ] Revisar nomes, referências e estado de conservação; melhorar acessibilidade e pesquisa com acentos.
