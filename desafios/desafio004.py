# Dissecando uma variável
algo = input('Digite algo: ')
print('O tipo primitivo dessa variavel é: ', type(algo))
print('A variavel contem somente espaços? ', algo.isspace())
print('A variavel é numerico?', algo.isnumeric())
print('A variavel é alfabetico?', algo.isalpha())
print('A variavel é alfanumerico?', algo.isalnum())
print('A variavel contem somente letras maiusculas?', algo.isupper())
print('A variavel contem somente letras minusculas?', algo.islower())
print('A variavel esta captalizada?', algo.istitle())


'''
tipos primitivos
int: 7 / -7/ 409898/ 0
float: 3.0/ 0.787875/ -15.0988/ 4.5
bool: True / False
str: 'Ola'/ '-9.5'/ ''
'''
