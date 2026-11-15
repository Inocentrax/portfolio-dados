"""Cria um trabalho sem sobrescrever arquivos e mantém seu registro no catálogo."""
import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'catalogo.json'


def slug(value):
    plain = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', plain).strip('-')


def render(entries):
    groups = [('Concluído', 'Demonstrações concluídas e verificadas'), ('Em andamento', 'Projetos em andamento'), ('Rascunho', 'Rascunhos e ideias'), ('Estudo', 'Estudos por assunto'), ('Versão de referência', 'Versões de referência')]
    text = '# Catálogo de projetos e estudos\n\n[Início](README.md) · [Próximos passos](PROXIMOS_PASSOS.md) · [Fluxo de trabalho](COMO_TRABALHAR.md)\n\nO status de cada entrada informa o estágio real do trabalho.\n'
    for status, title in groups:
        selected = [e for e in entries if e['status'] == status]
        if not selected:
            continue
        text += f'\n## {title} ({len(selected)})\n\n| Conteúdo | Status | Próximo passo |\n|---|---|---|\n'
        for e in selected:
            name = e['title'].replace('|', '/')
            action = e['action'].split(';')[0].split('.')[0].replace('|', '/')
            text += f'| [{name}]({e["path"]}/) | {status} | {action} |\n'
    return text


def check(entries):
    paths = [e['path'] for e in entries]
    if len(paths) != len(set(paths)):
        raise ValueError('Há caminhos repetidos no catálogo.')
    for e in entries:
        folder = ROOT / e['path']
        folder.resolve().relative_to(ROOT.resolve())
        assert (folder / 'README.md').is_file(), f'README ausente: {folder}'
        nb_path = ROOT / e['notebook']
        nb_path.resolve().relative_to(ROOT.resolve())
        nb = json.loads(nb_path.read_text(encoding='utf-8'))
        assert nb['nbformat'] == 4 and isinstance(nb['cells'], list)
    print(f'{len(entries)} entradas verificadas: pastas, READMEs e notebooks presentes.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('verificar')
    sub.add_parser('atualizar')
    new = sub.add_parser('novo')
    new.add_argument('titulo')
    new.add_argument('--area', default='geral')
    new.add_argument('--status', choices=['Rascunho', 'Em andamento', 'Estudo'], default='Rascunho')
    new.add_argument('--proximo-passo', default='Definir pergunta, dados e primeira entrega.')
    new.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    entries = json.loads(CATALOG.read_text(encoding='utf-8'))
    if args.command == 'verificar':
        check(entries)
        return
    if args.command == 'novo':
        name, area = slug(args.titulo), slug(args.area)
        if not name or not area:
            parser.error('Use título e área com letras ou números.')
        section = {'Rascunho': 'em-andamento', 'Em andamento': 'projetos', 'Estudo': 'estudos'}[args.status]
        rel = f'{section}/{area}/{name}'
        folder = ROOT / rel
        folder.resolve().relative_to(ROOT.resolve())
        if folder.exists() or any(e['path'] == rel for e in entries):
            parser.error('Este trabalho já existe. Retome sua pasta ou escolha outro nome.')
        if args.dry_run:
            print(f'Criaria {rel}/ e registraria no catálogo. Nenhum arquivo alterado.')
            return
        notebook = json.loads((ROOT / 'templates/notebook.ipynb').read_text(encoding='utf-8'))
        notebook['cells'][0]['source'] = f'# {args.titulo}\n\n**Status:** {args.status}\n\n## Objetivo\n\nDefinir pergunta e escopo.'
        readme = (ROOT / 'templates/PROJETO.md').read_text(encoding='utf-8').replace('# Nome do projeto', '# ' + args.titulo, 1).replace('**Status:** Rascunho.', f'**Status:** {args.status}.', 1)
        folder.mkdir(parents=True, exist_ok=False)
        (folder / 'README.md').write_text(readme, encoding='utf-8')
        (folder / 'notebook.ipynb').write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        entries.append({'title': args.titulo, 'originalTitle': args.titulo, 'status': args.status, 'classification': 'Novo', 'path': rel, 'notebook': rel + '/notebook.ipynb', 'action': args.proximo_passo, 'dependencies': []})
        CATALOG.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        with (ROOT / 'PROXIMOS_PASSOS.md').open('a', encoding='utf-8') as file:
            file.write(f'\n### [{args.titulo}]({rel}/)\n\n- [ ] {args.proximo_passo}\n')
        print(f'Trabalho criado: {rel}/. Revise os arquivos e faça um commit.')
    check(entries)
    (ROOT / 'CATALOGO.md').write_text(render(entries), encoding='utf-8')
    print('CATALOGO.md atualizado a partir de catalogo.json.')


if __name__ == '__main__':
    main()
