#-Comentários sobre python
#-Comentários podem ser usados para explicar o código Python.
#-Comentários podem ser usados para tornar o código mais legivel.
#-comentários podem ser usados para impedir a execuçao ao testar o código.

#-Criando comentários com a # e o python ira ignorá-los:

#-Exemplo
#This is a comment
print('hello, world!')
#-Os comentários podem ser colocados no final de uma linha e o python irá ignora o resto da linha:

print('Hello, world!') #This is a comment

#-Um comentário não precisa ser um texto que explique o código, ele também pode ser usado para evitar que o python execute o código:

#-Exemplo

#print('Hello, world!')
print('Cheers, Mate!')

#-Comentários multilinhas
#-na verdade, o python não possui uma sintaxe para comentarios multilinhas.

#-Para adicionar um comentário multilinha você pode inserir um # para cada linha:

#-EXEMPLO

#this is a comment
#written in
#more than just one line
print('Hello, world!')

#-ou não exatamente como pretendido, voce pode usar uma string multilinha.
#-Como no Python irá ignorar literais de string que não estão atribuidos a uma variável, voce pode adicionar uma string multilinha (aspas triplas) em seu código e colocar seu comentario dentro dela:

#-EXEMPLO
'''
this is a comment
written in
more than just one line
'''
print('Hello, world!')

#-Contanto que a string não seja atribuida a nenhuma variável, o Python lerá o código de várias linhas.

