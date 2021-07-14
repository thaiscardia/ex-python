"""Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequencia de Fibonacci."""

n = int(input("Insira número inteiro: "))

v1 = 1
v2 = 1

if n == 1 or n == 2: print("O resultado é 1.")
else:
    contador = 3
    lista = [0, 1, 1]
    while contador <= n:
        calculo = v1 + v2
        v2 = v1
        v1 = calculo
        contador += 1
        lista.append(calculo)

inicio = 0
fim = n
if len(lista) > n:
    print("A sequência de Fibonacci para o número {} é: {}".format(n, lista[0:fim]))