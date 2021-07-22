"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
No final, mostre:
a) quantas vezes apareceu o valor 9;
b) em que posição foi digitado o primeiro valor 3;
c) quais foram os números pares.
"""
n1 = int(input("Digite número 1: "))
n2 = int(input("Digite número 2: "))
n3 = int(input("Digite número 3: "))
n4 = int(input("Digite número 4: "))

contador = 0

tupla = (n1, n2, n3, n4)
pares = []
for i in tupla:
    if i % 2 == 0:
        pares.append(i)
    if i == 9:
        contador += 1
    if i == 3:
        print(f"O número 3 apareceu pela primeira vez na posição {tupla.index(3)+1}")
print(f"o(s) número(s) {pares} são pares")
print(f"O número 9 foi digitado {contador} vezes")
