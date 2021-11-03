"""
Escopo de Variáveis

Dois casos de escopo:

1 - Variáveis globais;
    -> Variáveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa.

2 - Variáveis locais;
    -> Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor


Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável
nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor da variável.

Em C:
int numero = 19

Em Java:
int numero = 19

Em Python:
numero = 19
"""

numero = 42    #Variável global
print(numero)

#Reatribuição
numero = 'Gabriel'
print(numero)


numero = 19

if numero > 17:
    novo = numero + 10
    print(novo)

numero1 = 16

if numero1 > 17:
    novo1 = numero1 + 10
    print(novo1)

else:
    print('Não é maior de idade')
    
    