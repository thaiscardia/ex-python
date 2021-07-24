"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = []
maior = menor = 0

for n in range(0, 5):
    lista.append(int(input(f"Digite número para posição {n}: ")))
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n] > maior: maior = lista[n]
        if lista[n] < menor: menor = lista[n]

print(f"O maior número digitado foi {max(lista)} na posição ", end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end="")
print()
print(f"O menor número digitado foi {min(lista)} na posição ", end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end="")
print()