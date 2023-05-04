
# The os module is used to interact operating system
# Doc: https://docs.python.org/3/library/os.html

import os
import sys

# os.system() permite executar comandos do sistema operacional a partir do seu código Python.

os.system('echo "Hello world"')
os.system('cls')  # 'clear' linux

# os.path trabalha com caminhos em Windows, Linux e Mac
# os.path.join: junta strings em um único caminho. Desse modo,

caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print('caminho')
print(caminho)

# os.path.split: divide um caminho uma tupla (diretório, arquivo).
diretorio, arquivo = os.path.split(caminho)
# os.path.exists: verifica se um caminho especificado existe.

print('O caminho existe?')
print(os.path.exists(caminho))

# separa a extesão do arquivo
nome_arquivo, extensao_arquivo = os.path.splitext(caminho)
print(f'nome do arquivo: {nome_arquivo}, extensao: {extensao_arquivo}')

# Caminho atual
print('O caminho atual')
print(os.path.abspath('.'))

# return the last dir component
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
# return dir
print(os.path.dirname(caminho))

# adiciona variavel de ambiente
sys.path.append('/home/marcio/projects/work/abi2/abi_project/dags')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'/home/teste.json'
