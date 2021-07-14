"""Refaça o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerra quando ele disser que quer mostrar 0 termos."""
from time import sleep

def calc():
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

def cont():
    continuar = int(input("Deseja visualizar mais termos? Digite 0 para encerrar programa. \n"))
    
    while continuar is not 0: 
        calc()
    print("Programa encerrado com sucesso!")

calc()
cont()