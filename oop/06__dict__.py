# __dict__ e vars para atributos de instância
# mostra os valores atribuido a classecle

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)

p1.nome = 'EITA'
print(vars(p1))
print(p1.nome)

# __dict__  també, altera os elementos 
print("----")
p1.__dict__['outra'] = 'coisa'
print(vars(p1))

print("----")
del p1.__dict__['nome']
print(vars(p1))

# p1.__dict__['nome'] = 'EITA'
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# print(p1.nome)

