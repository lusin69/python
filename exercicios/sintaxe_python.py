#-Sintaxe Python
#-Executar sintaxe Python
#-Como aprendemos na pagina anterior, a sintaxe pode ser executada escrevendo diretamente na linha de comando:
#>>> print('Hello, world!')
#-Hello, world!
#-Ou criando um arquivo python no servidor, usando a extensão de arquivo .py e executando-o na linha de comando:
#-C:\Users\Your Name>python myfile.py

#-Recuo Python
#-O recuo refere-se aos espaços no inicio de uma linha de codigo.
#-Enquanto em outras linguagens de programação o recuo no codigo é apenas para facilitar a leitura, o recuo em python é muito importante.
#-Python usa recuo para indicar um bloco de código.

#-EXEMPLO
if 5 > 2:
    print('Five is greater than two!')

#Python apresentará um erro se você pular o recuo:

#-EXEMPLO
#-Erro de sintaxe
if 5 > 2:
print('Fie is greater than two!')

#-A quantidade de espaços fica a seu criterio como programador, mais comum é quatro, mas tem que ser pelo menos um.

#-EXEMPLO

if 5 > 2:
    print('Five is greater than two!')
if 5 > 2:
        print('Five is greater than two!')

#-Voce deve usar o mesmo numero de espaços no mesmo bloco de código, caso contrário o o Python apresentará um erro:

#-EXEMPLO
#-Erro de sintaxe:

if 5 > 2:
 print('Five is greater than two!')
        print('Five is greater than two!')
 
#-Variáveis em Python
x = 5
y = 'hello, world!'

#-Python não possui comando para declarar uma variável.
#-Você aprenderá mais sobre variáveis no capitulo de variáveis do Python.

#Comentários
#-Python possui capacidade de comentários para fins de documentação noo código.
#-Os comentários começam com # e o Python renderizará o resto da linha como um comentário:

#EXEMPLO
#-Comentários em Python:

#This is a comment.
print('Hello, world!')

