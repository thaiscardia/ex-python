#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados por unidade, dezena, centena e milhar.
n = int(input("Digite número inteiro: "))

u = (n // 1) % 10
d = (n // 10) % 10
c = (n // 100) % 10
m = (n // 1000) % 10

print("Número digitado {}. \n Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}.".format(n, u, d, c, m))
