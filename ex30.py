#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import calendar

d = int(input("Digite o ano: "))
b = calendar.isleap(d)

if b == True:
    print("O ano {} é bissexto.".format(d))
else:
    print("O ano {} não é bissexto.".format(d))