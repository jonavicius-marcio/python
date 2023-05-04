
# Path ajuste the path to all operacional system
# Path Create paths in memory not fisical files

from pathlib import Path
from shutil import rmtree
caminho_projeto = Path()

print("print the absolute path")
print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
print("get the file path")
print(caminho_arquivo)

print("get parent")
print(caminho_arquivo.parent.parent)


print("create a new path and file name - doesn´t create the fisical file and paht ")
ideia = caminho_arquivo.parent.parent / 'ideia'
print(ideia / 'arquivo.txtcle')

print('home')
print(Path.home())

# Caminho atual
print('Create file')
create_file = Path().absolute() / 'arquivo.txt'
print(create_file)


# create file
print('Create file')
create_file = Path().absolute() / 'arquivo.txt'
create_file.touch()
print(create_file)

# write
print('write and read in the file')
create_file.write_text('olá mundo')
print(create_file.read_text())
# delete file
print('delete file')
create_file.unlink()

# Other away to create the files
file_path = Path().absolute() / 'another'
file_path.mkdir(exist_ok=True)


# Metthods
caminho_pasta = Path()
files = caminho_pasta / 'file'
files.mkdir(exist_ok=True)

# delete a  file if exist
for i in range(10):
    file = files / f'file_{i}.txt'

    # if file.is_file() # bolean
    # if file.is_dir() # bolean
    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('ola mundo \n')
        text_file.write(f'file_{i}.txt')
# Remove all files created
# rmtree(file)
