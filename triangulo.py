#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input("Digite comprimento da primeira reta: "))
b = float(input("Digite comprimento da segunda reta: "))
c = float(input("Digite comprimento da terceira reta: "))

if a + b > c or a + c > b or b + c > a:
    print("As medidas para os três segmentos informados \033[31mNÃO\033[m podem formar um triângulo")
else:
    print("A medida dos três segmentos informados \033[32mpodem\033[m formar um triângulo")
