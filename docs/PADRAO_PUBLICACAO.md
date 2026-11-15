# Padrão de organização e publicação

Aplicar aos repositórios existentes primeiro e depois aos projetos vindos do Drive. Cada arquivo deve ter uma função clara. A estrutura será proporcional ao projeto: exercícios curtos não precisam de pastas vazias nem infraestrutura artificial.

## Página inicial de cada projeto

O início do README deve trazer:

1. Título descritivo e uma frase que diga o que o projeto faz.
2. Problema ou pergunta analisada e contexto dos dados.
3. Principal resultado verificado, acompanhado de um gráfico legível ou demonstração quando útil. Se o projeto ainda não estiver concluído, declarar o estado real e as partes disponíveis.
4. Tecnologias utilizadas e link para o notebook ou ponto de entrada.

Depois, incluir dados e origem, metodologia, decisões de preparação, resultados, limitações, reprodução e créditos. Evitar badges decorativos que indiquem validações inexistentes. A descrição curta do repositório deve explicar o assunto em linguagem natural, sem repetir apenas o nome.

## Estrutura interna de cada notebook

1. **Título e resumo:** o que faz, pergunta, escopo e se é projeto, estudo ou exercício.
2. **Dados:** origem, período, unidade de observação, campos principais, tamanho e natureza real/sintética. Caminho de obtenção ou amostra redistribuível.
3. **Ambiente:** versão de Python e dependências efetivamente verificadas; instruções de preparação e entrada dos dados.
4. **Exploração e preparação:** explicar por que remover, preencher, transformar ou selecionar dados; mostrar impacto em linhas/colunas.
5. **Análise ou modelagem:** sequência única de cima para baixo. Experimentos comparados usam critérios compatíveis.
6. **Avaliação:** métricas e figuras calculadas pelo próprio código, com conjunto avaliado identificado. Quando houver ML supervisionado, separar treino/validação/teste e ajustar transformações apenas nos dados apropriados.
7. **Conclusão:** responder à pergunta com números observados, limitações e próximos passos. Nenhum X/Y ou texto de exemplo apresentado como achado real.
8. **Créditos:** autores/coautores, curso, livro, dataset e origem de imagens conforme aplicável.

Converter texto solto em código para Markdown. Padronizar títulos, ortografia, nomes de variáveis e unidades. Remover células vazias, instalações duplicadas e repetições sem papel didático. Exemplos intencionalmente incorretos devem explicar e capturar o erro para não interromper Executar tudo.

## Arquivos e pastas

Estrutura de referência, criando somente o que o projeto usa:

```text
nome-descritivo-do-projeto/
  README.md
  requirements.txt             # ou arquivo equivalente de ambiente verificado
  .gitignore
  notebooks/
    01_exploracao.ipynb
    02_modelagem.ipynb         # se houver modelagem
  data/
    README.md                 # origem, versão, esquema e obtenção
    sample/                   # apenas se puder redistribuir
  assets/
    resultado-principal.png
  src/                        # quando extrair código reutilizável fizer sentido
```

Arquivos usam nomes simples e descritivos, sem Untitled, Cópia de Cópia ou barras no nome. Usar .ipynb para notebooks e .py somente para scripts de fato. Evitar renomear repositórios publicados sem considerar URLs existentes. Documentos antigos e backups não devem competir com a versão principal na página inicial.

Cada arquivo tem um destino: notebook explica análise, script informa como executar, dado tem origem/esquema, figura tem título/unidade e uso na documentação. Remover arquivos redundantes da apresentação somente após preservar conteúdo útil.

## Reprodução e resultados

- Reiniciar o ambiente e executar sequencialmente com as dependências e dados documentados.
- Evitar depender de variáveis definidas em outro notebook ou de caminhos particulares /content/drive/MyDrive.
- Parametrizar entradas; tornar criação de arquivos e diretórios repetível sem apagar conteúdo do usuário.
- Para ML, registrar seeds, divisão, baseline, métricas fora do treino e limitações. Comparar alternativas na mesma divisão.
- Salvar transformação e modelo juntos quando existir inferência posterior.
- Figuras com título, eixos, unidades e legenda; incluir versão estática quando a visualização interativa não aparecer no GitHub.
- Registrar o que foi executado e o que ficou pendente. Executar sem erro não comprova validade metodológica: conferir também significado das métricas e conclusões.

## Autoria e dados

Conservar coautoria e atribuição a cursos/livros. Escolher licença de código somente após confirmar direitos sobre o conteúdo; documentar separadamente a licença dos dados. Substituir exemplos pessoais por dados sintéticos e revisar outputs antes de tornar público. Não enviar dados privados ou credenciais ao repositório.

## Critério de conclusão

Um item fica pronto quando alguém sem contexto consegue entender o projeto, encontrar o ponto de entrada, obter os dados permitidos, reproduzir o fluxo documentado e conferir a conclusão. Estudos podem ser curtos, desde que o propósito e os limites estejam claros.
