#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input("Digite primeiro número: "))
n2 = float(input("Digite segundo número: "))
n3 = float(input("Digite terceiro número: "))

l = [n1, n2, n3]

print("O maior número é {} e o menor número é {}".format(max(l), min(l)))