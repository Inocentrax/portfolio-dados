# Verificação da organização

Data: 15/11/2026.

## Cobertura

- 69 entradas no catálogo, cada uma com README e notebook.
- 39 estudos, 12 projetos em andamento, 7 rascunhos e 11 versões de referência.
- 70 notebooks JSON válidos contando o modelo de criação.
- 1.468 células de código com sintaxe Python verificada, desconsiderando linhas de comandos específicos de Colab/Jupyter.
- Links locais dos READMEs e catálogo conferidos: nenhum destino ausente.
- Outputs e contadores de execução antigos retirados; metadados pessoais do Colab não foram migrados.

## Execução local

22 notebooks de exemplos locais foram executados sequencialmente. Os que dependem de rede, datasets externos, entradas interativas ou bibliotecas de ML não foram executados nesta migração. Um estudo de DataFrame teve as primeiras 17 células executadas, mas a visualização final não foi concluída por ausência de Matplotlib no ambiente; a dependência está declarada.

Ambiente usado: Python 3.12.14, pandas 3.0.1, NumPy 2.3.5. Dependências declaradas nos demais projetos ainda precisam de combinação de versões verificada.

### Amostra de alunos

O exemplo revisado foi executado com os dados versionados sem nomes: 18 registros, 6 notas ausentes, média observada 6,80, mínimo 2,5, máximo 10,0 e 8 aprovações informadas. As notas ausentes continuam ausentes no cenário; o bônus é limitado a 10. Origem externa e regra original de aprovação continuam como pendências.

## Limites

A publicação organiza o trabalho e torna seus próximos passos visíveis. Ela não certifica que todos os modelos estão corretos nem transforma trabalhos incompletos em concluídos. Conclusões de dados externos, licenças, compatibilidade de ML e resultados completos serão verificados ao desenvolver cada projeto.

## Segunda etapa — demonstrações verificadas

Em 15/11/2026 foram executados os scripts completos de classificação de dígitos e análise imobiliária. Os requisitos exatos, parâmetros, resultados e limitações estão nas respectivas pastas.

- Dígitos: divisão estratificada sem sobreposição, scaler ajustado no treino, baseline, logística e MLP avaliados nas 360 amostras reservadas; métricas finitas e no intervalo esperado.
- Aluguéis: revisão fixa da base com hash verificado; filtros de área/aluguel positivos, ausências preservadas e rankings com suporte mínimo.
- Cinco figuras geradas e inspecionadas visualmente.
- As bases de terceiros encontradas no Drive não tiveram sua visibilidade alterada e não foram copiadas em massa para o GitHub.

O ambiente adicional de execução foi instalado em uma pasta isolada do workspace. Dados em cache e pacotes não fazem parte da publicação.

As versões finais dos dois notebooks também foram executadas integralmente, além dos scripts equivalentes; os 70 notebooks passaram na validação de esquema nbformat.

## VGSales — continuidade após envio dos dados

Arquivo enviado conferido por conteúdo e checksum com a versão arquivada. Análise executada com os 16.598 registros preservados; 271 ausências de ano e 58 de editora tratadas conforme o uso. Agregações de plataforma/editora conservam o total global e as participações de gênero somam 100% por região. Quatro gráficos foram inspecionados visualmente. O ano é tratado como lançamento, não como calendário de transações.

O catálogo mantém 69 trabalhos ativos: 3 demonstrações concluídas, 10 em andamento, 6 rascunhos, 39 estudos e 11 versões de referência. O endereço antigo do notebook de videogames contém apenas uma orientação de mudança, sem duplicar o desenvolvimento.
