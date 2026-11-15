"""Obtém exatamente a base já publicada no repositório original."""
from hashlib import sha1
from pathlib import Path
from urllib.request import urlopen

URL = 'https://raw.githubusercontent.com/Inocentrax/Amazon-Vendas-India/5dd724d7854385563bb9c0493e2b0191bb6029ec/AmazonSaleReport.csv'
GIT_BLOB_SHA = '6e44bab59f8f990255a871f25e4255397c63cb3c'

def verificar(data):
    digest = sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    if digest != GIT_BLOB_SHA:
        raise ValueError('A base difere da versão original esperada.')

if __name__ == '__main__':
    target = Path(__file__).resolve().parent / 'AmazonSaleReport.csv'
    if target.exists():
        verificar(target.read_bytes())
    else:
        with urlopen(URL, timeout=120) as response:
            data = response.read()
        verificar(data)
        target.write_bytes(data)
    print(f'Base verificada: {target}')
