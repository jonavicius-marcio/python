
# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os
from pathlib import Path

# Create path
caminho_atual = Path().absolute()
caminho = caminho_atual / 'arquivos'
caminho.mkdir(exist_ok=True)

# Create files
for i in range(10):
    file = caminho / f'file_{i}.txt'
    file.touch()

print(f'list files: {os.listdir(caminho_atual)}')

# list files
for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)
