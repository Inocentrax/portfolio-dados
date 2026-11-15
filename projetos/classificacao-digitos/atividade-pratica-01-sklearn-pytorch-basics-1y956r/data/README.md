# Dados — Digits

Carregados com sklearn.datasets.load_digits, sem arquivos privados do Drive. O experimento usa 1797 imagens 8×8, com classes de 0 a 9. A descrição e as referências da coleção estão em load_digits().DESCR.

A divisão é estratificada 80/20 com semente 42. O hash SHA-256 dos índices de teste, codificados como inteiros little-endian de 64 bits, está em resultados.json. A padronização é ajustada exclusivamente no treino.
