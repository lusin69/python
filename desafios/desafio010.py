# Crie um programa que que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 4.99
euro = real / 5.40
print('com R${:.2f} você pode comprar em dolares US${:.2f} em euros EUR{:.2f}'.format(real, dolar, euro))