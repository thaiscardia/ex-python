"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. """

pesos = []
for p in range(0, 5):
    p = float(input("Insira o peso: "))
    pesos.append(p)


print("O maior peso digitado foi {} e o menor peso digitado foi {}.".format(max(pesos), min(pesos)))