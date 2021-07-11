"""Faça um programa que mostre na tela uma contagem regressiva para o estouro
de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles"""
from time import sleep

print("Contagem para os fogos de artifício:")
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print("\033[32mB\033[m\033[31mU\033[mU\033[32mU\033[m\033[31mU\033[mM")