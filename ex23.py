#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
n = input("Digite seu nome: ")
sp = n.split()
search = "Silva"

if search in sp:
    print("Você possui Silva no seu nome.")

else:
    print("Você não possui Silva no seu nome.")
