"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços"""
from time import sleep

frase = str(input("Insira sua frase: ")).strip().upper()
print("Vamos conferir se é um palíndromo...")
sleep(2)

divisao = frase.split()
junto = ''.join(divisao)
inversao = ''
for l in range(len(junto) - 1, -1, -1):
    inversao += junto[l]

if inversao == junto:
    print("A palavra é um palíndromo! Veja: O digitado é {} e o inverso é {}".format(frase, inversao))
else:
    print("A palavra não é um palíndromo")