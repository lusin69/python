# Atribuir vários valores
# Muitos valores para múltiplas variáveis
# Python pernite atribuir valores a múltiplas variaveis em uma linha:

#EXEMPLO

x, y, z = 'Orange', 'Banana', 'Cherry'
print(x)
print(y)
print(z)
'''
Nota certifique-se de que o numero de variáveis corresponda ao numero de valores, caso contrário você receberá um erro.
'''
# um valor para multiplas variáveis
# E você pode atribuir o mesmo valor a múltiplas variáveis em uma linha:

# EXEMPLO

x = y = z = 'Orange'
print(x)
print(y)
print(z)

# Descompacte uma coleção
# Se você tiver uma coleção de valores em uma lista, tupla etc. Python permite extrair os valores em variáveis. Isso é chamado de descompactação.

#EXEMPLO

# Descompacte uma lista:
fruits = ['apple', 'banana', 'cherry'] 
x,y,z = fruits
print(x)
print(y)
print(z)
