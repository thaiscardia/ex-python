"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo"""
pr = int(input("Insira um número inteiro: "))

if pr > 2 and pr % 2 == 0 or pr > 3 and pr % 3 == 0 or pr > 5 and pr % 5 == 0 or pr > 7 and pr % 7 == 0:
    print("Não é número primo")
elif pr == 1: print("Não é número primo")
else:
    print("É número primo")