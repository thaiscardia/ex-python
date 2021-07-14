"""Crie um programa que leia 2 valores e mostre na tela um menu:
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso
"""
from time import sleep
v1 = float(input("Insira valor 1: "))
v2 = float(input("Insira valor 2: "))
menu=0

while menu != 5:
    menu = int(input("Escolha opção: \n[1] somar \n[2] multiplicar \n[3] maior \n[4] novos numeros \n[5] sair do programa \n"))
    if menu == 1:
        soma = v1 + v2
        print("A soma dos valores é: {}".format(soma))
    elif menu == 2:
        mult = v1 * v2
        print("A multiplicação dos valores é: {}".format(mult))
    elif menu == 3:
        maior = [v1, v2]
        print("O valor {} é maior que o valor {}".format(max(maior), min(maior)))
    elif menu == 4:
        v1 = float(input("Insira valor 1: "))
        v2 = float(input("Insira valor 2: "))
        print(menu)
    elif menu == 5:
        print("Encerrando...")
    else:
        print("Opção inválida. Tente Novamente.")
    sleep(2)
print("Programa encerrado!")

