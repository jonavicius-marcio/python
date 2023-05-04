
# The os module is used to interact operating system
# Doc: https://docs.python.org/3/library/os.html


# os.walk para navegar de caminhos de forma recursiva
# os.listdir para navegar em caminhos

import os
from pathlib import Path
from itertools import count

# Create path
caminho_atual = Path().absolute()
caminho = caminho_atual / 'arquivos'
caminho.mkdir(exist_ok=True)

# Create files
for i in range(10):
    file = caminho / f'file_{i}.txt'
    file.touch()

print(f'list files: {os.listdir(caminho_atual)}')

counter = count()

print(Path().absolute())

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print('  ', the_counter, 'FILE:', caminho_completo_arquivo)
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)
