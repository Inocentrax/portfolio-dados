# Extinção animal — busca de espécies

Aplicação de estudo em HTML, CSS e JavaScript para pesquisar uma base local de espécies por nome, descrição e tags.

**Status:** Projeto de estudo · conteúdo em revisão.

[← Catálogo de projetos e estudos](../../README.md)

---

Página de pesquisa com cartões de espécies e links de referência. O foco técnico é praticar busca textual e renderização no navegador.

## Como usar

Abra [index.html](index.html), digite um termo e clique em **Pesquisar**. A pesquisa consulta nome, descrição e tags de uma base local; não exige backend.

## Estrutura

| Arquivo | Função |
|---|---|
| [app.js](app.js) | Pesquisa e montagem dos resultados |
| [dados.js](dados.js) | Base editorial de espécies |
| [style.css](style.css) | Aparência e layout |
| [index.html](index.html) | Página inicial |

## Limites e evolução

A base editorial precisa de revisão de nomes, duplicatas e estado de conservação. O título da aplicação não deve ser interpretado como validação científica de todos os registros.

- [ ] Revisar cada entrada e suas referências.
- [ ] Distinguir extinção global, extinção local e espécies ameaçadas.
- [ ] Consolidar nomes repetidos e sinônimos.
- [ ] Melhorar acessibilidade e pesquisa com acentos.

## Créditos

O README original informa que a imagem de fundo foi produzida com Leonardo.ai. Os registros apontam para referências na Wikipédia. O endereço de demonstração registrado no projeto é [animais-extintos.vercel.app](https://animais-extintos.vercel.app/); sua disponibilidade não foi verificada nesta organização.

## Continuidade no portfólio

Esta pasta é a versão de referência para continuar o trabalho. O [repositório original](https://github.com/Inocentrax/Animais-Extintos) conserva seu histórico anterior.

[Catálogo](../../CATALOGO.md) · [Próximos passos](../../PROXIMOS_PASSOS.md)
