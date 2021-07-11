"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
Considere 21 anos como maioridade. """

idades = []
for pessoa in range(0, 7):
    pessoa = int(input("Insira a idade: "))
    idades.append(pessoa)

maior = []
menor = []
for i in idades:
    if i >= 21:
        maior.append(1)
    else:
        menor.append(1)
        
maiores = sum(maior)
menores = sum(menor)

print("Há {} maiores de idade e {} menores de idade.".format(maiores, menores))