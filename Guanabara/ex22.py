#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
n = input("Digite o nome da uma cidade: ")
sp = n.split()

if sp[0] == "Santo":
    print("A cidade {} começa com o nome Santo.".format(n))
else:
    print("A cidade {} não começa com o nome Santo".format(n))