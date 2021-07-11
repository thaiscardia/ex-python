"""Refaça o desafio dos triangulos acrescentando o recurso de mostrar que tipo de triangulo será formado:
-equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes"""

a = float(input("Digite comprimento da primeira reta: "))
b = float(input("Digite comprimento da segunda reta: "))
c = float(input("Digite comprimento da terceira reta: "))

#pré requisito: cada um dos lados não podem ser maior do que a hipotenusa
if a + b > c and a + c > b and b + c > a: 
    if a == b and b == c: print("As medidas para os três segmentos informados \033[31mPODEM\033[m formar um triângulo EQUILÁTERO")
    elif a != b and b != c: print("As medidas para os três segmentos informados \033[31mPODEM\033[m formar um triângulo ESCALENO")
    else: print("As medidas para os três segmentos informados \033[31mPODEM\033[m formar um triângulo ISÓCELES")
else: print("A medida dos três segmentos informados \033[32mNÃO PODEM\033[m formar um triângulo")