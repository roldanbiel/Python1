"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: Os separados de casas decimais na programação é o ponto e não a vírgula.
"""

# Errado ao ponto do Float, gera Tupla
valor = 1, 44
print(type(valor))

# Correto ao ponto Float
valor = 1.44
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(valor2)

# Podemos converter um float para int
"""
OBS: Ao converter valores float para int perde-se precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
valor3 = 5j
print(type(valor3))