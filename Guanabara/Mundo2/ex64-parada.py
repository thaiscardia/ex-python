"""Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)"""

num = int(input("Insira número: "))
lista = [num]
contador = 0

while num != 999:
    num = int(input("Número inserido. Insira número: "))
    contador += 1
    lista.append(num)
lista.pop(-1) #desconsiderando o ultimo numero digitado
contador -= 1 #desconsiderando a flag de parada
soma = sum(lista)
print("Programa encerrado! Você digitou um total de {} números e a soma entre eles é de {}".format(contador, soma))