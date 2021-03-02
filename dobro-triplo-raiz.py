# crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
n = float(input("Digite um número: "))

from math import sqrt
d = n * 2
t = n * 3
sr = math.sqrt(n)

print("O dobro do número {} é {}, o triplo é {} e sua raiz quadrada é {}".format(n, d, t, sr))