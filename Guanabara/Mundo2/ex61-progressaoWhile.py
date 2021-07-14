"""Refaça o DESAFIO 51 lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while."""

ter = int(input("Insira primeiro termo da P.A: "))
ra = int(input("Insira a razão: "))

lista = []
limite = 0

while limite is not 11:
    calc = ter + (limite - 1) * ra
    lista.append(calc)
    limite += 1
lista.pop(0)
print(lista)