""" Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor dos valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. """
from time import sleep


num = int(input("Insira número: "))
lista = [num]
contador = 1
continuar = str(input("Deseja continuar? \n")).strip().upper()[0]
media = 0

while continuar not in "Y":
    num = int(input("Número inserido. Insira número: "))
    lista.append(num)
    contador += 1
    continuar = str(input("Deseja continuar? \n")).strip().upper()[0]
elif continuar in "N" and continuar not in "Y":
    sleep(2)
    media = sum(lista)/contador
    print("Programa encerrado com sucesso!")
    print("A média de valores é de {}. O valor mais alto digitado foi {} e o mais baixo foi {}.".format(media, max(lista), min(lista)))
else: print("Opção inválida. Tente novamente.")