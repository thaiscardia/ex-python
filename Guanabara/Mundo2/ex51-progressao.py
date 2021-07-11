"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão"""

ter = float(input("Insira primeiro termo da P.A: "))
ra = float(input("Insira a razão: "))

lista = []
for c in range (1, 11):
    calc = ter + (c - 1) * ra
    lista.append(calc)
print(lista)