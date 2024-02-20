# Variáveis de saída
# A função print() é frequentemente usada para gerar variáveis.

#EXEMPLO
x = 'Python is awesome'

# Na função print(), você gera múltiplas variáveis, separadas por virgula:

#EXEMPLO

x = 'Python'
y = 'is'
z = 'awesome'
print(x, y, z) # Python is awesome

# Voce também pode usar o operador + para gerar multiplas variáveis:

#EXEMPLO

x = 'Python '
y = 'is '
z = 'awesome '
print(x + y + z) # Python is awesome

''' Observação o caractere de espaço depois de 'Python ' e 'is ', sem eles os resultados seriam 'Pythonisawesome'.
'''
# Para os números, o caractere + funciona como um operador matemático:

#EXEMPLO

x = 5
y = 10
print(x + y) # 5+10=15

# Na funcao print(), ao tentar combinar uma string e um numero com o operador +, o python aprensentará um erro:

# EXEMPLO

x = 5
y = 'John'
print(x + y) 
#TypeError: tipos de operandos não suportados para +: 'int' e 'str'
 ''' A melhor forma de gerar múltiplas variáveis na função print() é separa-las com vírgulas, que suportam ate mesmo diferentes tipos de dados:'''

# EXEMPLO

x = 5
y = 'John'
print(x, y) # 5 joão




