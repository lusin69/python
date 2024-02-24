# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta , pinta uma área de 2m².
largura = float(input('Digite a largura da parede: ')) 
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print('Sua parede tem a dimenção de {}m x {}m e a sua area é {}m².'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede você precisa-ra de {}L'.format(tinta))
