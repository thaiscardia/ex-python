#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input("Digite um número inteiro: "))
e = int(input("Escolha a base de conversão: \n Digite 1 para Binário: \n Digite 2 para Octal: \n Digite 3 para Hexadecimal: \n"))

if e == 1:
    print("Seu número em binário é: {}".format(bin(n)[2:]))
elif e == 2:
    print("Seu número em octal é: {}.".format(oct(n)[2:]))
elif e == 3:
    print("Seu número em hexadecimal é: {}.".format(hex(n)[2:]))
else:
    print("Entrada incorreta")