#-Variáveis _ _ _ _
#-Variáveis são contêineres para armazenar valores de dados.

#-Criando Variáveis

#-Python não possui comando para declarar uma variável.
#-Uma variável é criada no momento em que você atribui um valor a ela pela primeira vez.

#-EXEMPLO
x = 5
y = 'John'
print(x)
print(y)

#-Variáveis não precisam ser declaradas com nenhum tipo específico e pode até mudar de tipo depois de terem sido definidas.

#EXEMPLO

x = 4   # x is of type int
x = 'Sally' # x is now of type str
print(x)

#-FUNDIÇÃO
#-Se você quiser especificar o tipo de dados, isso pode ser feito com conversão

#EXEMPLO

x = str(3)      # x will be '3'
y = int(3)      # y will be 3
z = float(3)    # z will be 3.0
print(x)
print(y)
print(z)

#-Obetenha o tipo
#-Você pode obter o tipo de dados de uma variável com a função type()

#EXEMPLO

x = 5 
y = 'John'
print(type(x))
print(type(y))

#-Aspas simples ou aspas duplas?

#-variáveis de string podem ser declaradas usando aspas simples ou duplas:

#EXEMPLO

x = "john"
# is The same as
x = 'john'

# Os nomes das variáveis diferenciam maiuscúlas de minúscula.

# EXEMPLO
# Isso criará duas variáveis:

a = 4
A = 'Sally'
# A will not overwrite a
