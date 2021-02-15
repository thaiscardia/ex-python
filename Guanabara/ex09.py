'''Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a qtd de tinta necessária para pintá-la, sabendo que cada
litro de tinta pinta uma área de 2m²'''
larg = float(input("Digite a largura em metros:"))
alt = float(input("Digite a altura em metros: "))
a = larg * alt
t = a / 2
print("Para pintar esta parede completamente, você precisará de {}L de tinta".format(t))