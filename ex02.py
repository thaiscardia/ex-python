#faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
num = int(input("Digite um número inteiro: "))
ant = num - 1
suc = num + 1

print("O sucessor do número {} é o número {}, e o anterior é o número {}".format(num, suc, ant))