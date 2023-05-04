# Variáveis de ambiente com Python

# Windows PS: $Env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL

# from dotenv import load_dotenv  # type: ignore
from dotenv import load_dotenv
import os

# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']

print(os.getenv('OneDrive'))
# os.system('$Env:valor="201"')

# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'

os.environ['valor'] = '201'


# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example


load_dotenv()
