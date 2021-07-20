""" Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor dos valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. """
from time import sleep


num = int(input("Insira número: "))
continuar = str(input("Deseja continuar? [S/N] \n")).strip().upper()[0]
lista = [num]
contador = 1
media = 0

while continuar == "S":
    num = int(input("Número inserido. Insira número: "))
    continuar = str(input("Deseja continuar? \n")).strip().upper()[0]
    lista.append(num)
    contador += 1
soma = sum(lista)
media = soma/contador
print("A média de valores é de {}. O valor mais alto digitado foi {} e o mais baixo foi {}.".format(media, max(lista), min(lista)))
