# Desenvolva um programa que leia as duas notas de um aluno. e em seguida calcule a sua media.
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('O aluno {} tirou na primeira prova {} \n Na segunda avaliação ele tirou {} \n ficando assim com a media de {:.2f}'.format(nome, nota1, nota2, media))
