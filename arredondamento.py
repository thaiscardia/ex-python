# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
n = float(input("Digite um número: "))
from math import trunc #truncate mostra apenas o numero inteiro, arredondando-o em direção ao zero (para cima ou para baixo)
print("O número inteiro é {}".format(trunc(n))) #outra opção é usar o int