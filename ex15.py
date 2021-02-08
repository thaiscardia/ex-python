#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#calcule e mostre o comprimento da hipotenusa.
a = float(input("Digite comprimento do cateto oposto: "))
b = float(input("Digite comprimento do cateto adjacente: "))
from math import sqrt as r

hip = r((a ** 2) + (b ** 2))

print("A hipotenusa é {}".format(hip))