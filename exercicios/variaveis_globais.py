# Variáveis criadas fora de uma função (como em todos os exemplos anteriores) são conhecidas como variáveis globais.
# Variáveis globais podem ser usadas por qualquer pessoa, tanto dentro quanto fora das funções.

# EXEMPLO
# Crie uma variavel fora de uma função e use-a dentro da função

x = 'awesome'

def myfunc(): # def(define uma função)
    print('Python is ' + x)

myfunc()    