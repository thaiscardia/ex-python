"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o"""
lista = []
for i in range(0, 6):
    num = int(input("Insira número inteiro: "))
    if num % 2 == 0: 
        lista.append(num)
soma = sum(lista)
print("A soma dos números pares inseridos é {}".format(soma))