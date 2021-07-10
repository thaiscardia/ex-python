"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente"""
n = input("Digite seu nome completo: ")
nSP = n.split()[0]
rev = n.split()[-1]

print("Seu primeiro nome é {} e seu último nome é {}.".format(nSP, rev))