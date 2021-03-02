# faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
vl = float(input("Digite o preço do produto: "))
pd = 5
dt = (vl * pd) / 100

print("O valor de seu produto com 5% de desconto é {}".format(vl - dt))
