''' crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode *comprar. Considere USD1 = R$3,27'''
v = float(input("Qual valor você possui? "))
c = v / 3.27
print("Você conseguirá comprar {:.2f} dólares".format(float(c))) #.Xf define quantas casas decimais após a virgula serão visualizados