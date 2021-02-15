''' Faça um programa que leia um numero inteiro qualquer e mostre na tela sua tabuada'''
num = int(input("Digite um número inteiro: "))

def tabuada(n):
    print("A tabuada de número {} é: ".format(num))
    for n in range(0,11): #range retorna uma sequencia de numeros, iniciando por 0 por padrão, adicionando +1 e para antes de um número especifico. Neste caso, 11 (para no 10).
        print ("{:2} * {:2} = {:2}".format(n, num, n * num))

tabuada(num)