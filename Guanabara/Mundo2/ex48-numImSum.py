"""Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500"""

lista = []
for i in range(0, 500, 3):
    if i % 3 == 0 and i % 2 != 0:
        lista.append(i)
soma = sum(lista)
print(soma)