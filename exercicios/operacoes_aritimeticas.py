# Operadores aritimeticos
'''
+ usado para adição ex: 5 + 2 == 7
- usado ára subtração ex: 5 - 2 == 3
* usado para multiplicação ex: 5 * 2 == 10
/ usado para divisão ex: 5 / 2 == 2.5
** usado para potencia ex: 5 ** 2 == 25 pow(5,2)
// usado para divisão inteira ex: 5 // 2 == 2
% usado para resto da divisão ex: 5 % 2 == 1
== usado como igualdade
= usada como recebe

'''
# Ordem de precedência
'''
1° () parenteses.
2° ** potencias. 
3° * / // % multiplicação, divisão, divisão inteira, resto da divisão.
4° + - adição e subtração
obs: para fazer raiz quadrada usa-se **(1/2) exemplo raiz quadrada de 9 ficaria assim: 9 ** (1/2) raiz cubica (1/3) raiz quarta (1/4)...
'''

# Fazendo operações
'''
5 + 3 * 2 == 11
3 * 5 + 4 ** 2 == 31
3 * (5 + 4) ** 2 == 243

'''
'''
'oi'*5== 'oioioioioioi'
'='*3== '==='
'''
# Usando operadores

nome1 = input('Digite seu nome: ')
print('Seja bem vindo {}!'.format(nome1))


nome2 = input('Digite seu nome: ')
print('Seja bem vindo {:20}!'.format(nome2)) #colocará 20 espaços apos o nome

nome3 = input('digite seu nome: ')
print('seja bem vindo {:>20}!'.format(nome3)) # alinhamento com sinal de maior coloca o nome pra direita em 20 espaços

nome4 = input('digite seu nome: ')
print('seja bem vindo {:>20}!'.format(nome4)) # alinhamento com o sinal de menor coloca o nome para a esquerda em 20 espaços

nome5 = input('Digite seu nome: ')
print('seja bem vindo {:^20}!'.format(nome5)) #alinhamento contral com o acento circunflexo em 20 de espaço

nome6 = input('Digite seu nome: ')
print('seja bem vindo {:=^20}!'.format(nome6)) # alinhamento central com sinais de = ao redor em 20 espaços

n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('a soma é {} o produto é {} e a divisão é {:.3f}'.format(s, m, d)) # :.3f quer dizer 3 numeros apos a virgula
print('a divisão inteira é {} e a potencia é {}'.format(di, p))

'''
\n 1uebra de linha
and='' ajutamento de linhas
'''
n3 = int(input('digite um valor: '))
n4 = int(input('digite outro valor: '))
s = n3 + n4
m = n3 * n4
d = n3 / n4
di = n3 // n4
p = n3 ** n4
print('a soma é {} o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ') # o end='' junta os print numa so linha
print('a divisão inteira é {} e a potencia é {}'.format(di, p))

n5 = int(input('digite um valor: '))
n6 = int(input('digite outro valor: '))
s = n5 + n6
m = n5 * n6
d = n5 / n6
di = n5 // n6
p = n5 ** n6
print('a soma é {} o produto é {} \n e a divisão é {:.3f}'.format(s, m, d)) # :.3f quer dizer 3 numeros apos a virgula
print('a divisão inteira é {} \n e a potencia é {}'.format(di, p))  # \n faz uma quebra de linha 
