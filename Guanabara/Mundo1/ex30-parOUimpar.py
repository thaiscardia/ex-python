#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
def consulta():
    n = int(input("Digite número inteiro: "))
  
    if n % 2 == int(0):
        print("Este número é par")
    else:
        print("Este número é impar")

consulta()
