#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#calcule e mostre o comprimento da hipotenusa.
a = float(input("Digite comprimento do cateto oposto: "))
b = float(input("Digite comprimento do cateto adjacente: "))
from math import hypot as h

hip = h(a, b)

print("A hipotenusa é {:.2f}".format(hip))