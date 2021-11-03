
"""
Recebendo dados do usuário. 

input() -> Todo dado recebido via input é do tipo String

Em Python, String é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Gabriel Roldan'
- Aspas duplas -> "Gabriel Roldan"
- Aspas simples triplas -> '''Gabriel Roldan'''

"""
# - Aspas duplas triplas -> """Gabriel Roldan"""


#Forma1 RECEBER:
# print("Qual seu nome? ")
# nome = input()   # Input -> Entrada de Dados

#Forma2 RECEBER:
nome = input('Qual seu nome? ')

#Forma PRINT:
print(f'Olá, {nome.title()}, seja bem-vindo!')

#Forma1 RECEBER:
# print("Qual sua idade? ")
# idade = input()

#Forma2 RECEBER
idade = int(input('Qual sua idade? '))
# ou
# idade = (input('Qual sua idade? '))  -> sem 'int' / sem cast
# se a saida for:
# print(f'{nome.title()} nasceu em {2021 - int(idade)}')


#Adicionado por mim
print(f'Nome: {nome.title()}')
print(f'Idade: {idade}')

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
#Adicionado por mim
print(f'{nome.title()} nasceu em {2021 - idade}')
if int(idade) > 17:
    #Forma PRINT:
    print(f'Parabéns, {nome.title()}, você é maior de idade!')

else:
    #Forma PRINT:
    print(f'Infelizmente você não é maior de idade, {nome.title()}.')


