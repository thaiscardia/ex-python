"""Faça um programa que leia um número qualquer e mostre o seu fatorial"""

from math import factorial

n = float(input("Insira um número: "))
print("O fatorial do número {} é: {}".format(n, factorial(n)))