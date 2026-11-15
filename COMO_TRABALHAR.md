# Trabalhar a partir do GitHub

## Retomar um notebook

1. Abra o catálogo e escolha a pasta do trabalho.
2. Leia as pendências e use **Abrir no Colab** no README.
3. Ao terminar, use no Colab **Arquivo → Salvar uma cópia no GitHub**. Selecione este repositório e **o mesmo caminho do notebook indicado no catálogo**.
4. Confira o diff antes de confirmar: não inclua credenciais nem dados privados.
5. Atualize o README da pasta e suas pendências.

O Colab funciona como ambiente de execução. O commit no GitHub é o ponto de continuidade; salvar apenas no Drive não atualiza este catálogo.

## Novo projeto

Crie uma pasta com nome descritivo em em-andamento/ ou projetos/, usando os [modelos](templates/). Um único tema tem uma pasta principal; experimentos relacionados podem ficar nela. Adicione a entrada ao catálogo e a próxima ação ao plano.

## Status

- **Rascunho:** ideia e preparação inicial; partes centrais ainda faltam.
- **Em andamento:** fluxo implementado em parte, com validações pendentes.
- **Estudo:** exercício ou explicação de técnica com escopo didático.
- **Concluído:** execução documentada, dados identificados e conclusões verificadas.
- **Versão de referência:** material anterior ou modelo; não é o ponto principal de desenvolvimento.

## Rotina para não perder projetos

No fim de uma sessão, registre no README: o que mudou, a próxima ação e qualquer impedimento. Faça um commit pequeno com mensagem descritiva. Evite Cópia de, Untitled e uma pasta nova para cada tentativa. O histórico do Git já preserva as revisões.

Para mudanças grandes, trabalhe em uma branch e revise antes de mesclar. Um projeto só muda para concluído após cumprir o [padrão de publicação](docs/PADRAO_PUBLICACAO.md).

## Criar e registrar pelo terminal

Na raiz do repositório:

```bash
python scripts/catalogo.py novo "Análise de energia" --area iot --status Rascunho
python scripts/catalogo.py verificar
```

O comando cria README e notebook usando os modelos, registra no catálogo e adiciona uma próxima ação. Ele recusa sobrescrever uma pasta existente. Use --dry-run para conferir o destino sem criar nada.

Ao mudar o status ou a próxima ação de um trabalho, atualize catalogo.json e o README da pasta e execute `python scripts/catalogo.py atualizar`. Depois revise o diff e faça o commit.
