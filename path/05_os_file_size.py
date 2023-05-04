
# The os module is used to interact operating system
# Doc: https://docs.python.org/3/library/os.html


# os.walk para navegar de caminhos de forma recursiva
# os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)
import math
import os
from itertools import count
from pathlib import Path


# Create path
caminho_atual = Path().absolute()
caminho = caminho_atual / 'arquivos'
caminho.mkdir(exist_ok=True)

# Create files
for i in range(10):
    file = caminho / f'file_{i}.txt'
    file.touch()


def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"

    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        # tamanho = os.path.getsize(caminho_completo_arquivo)
        stats = os.stat(caminho_completo_arquivo)
        tamanho = stats.st_size
        print('  ', the_counter, 'FILE:', file_, formata_tamanho(tamanho))
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)
