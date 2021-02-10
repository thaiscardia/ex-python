"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas as letras minúsculas;
- Quantas letras tem ao todo;
- Quantas letras tem o primeiro nome. """

n = input("Digite seu nome completo: ")
ma = n.upper()
mi = n.lower()
np = n.replace(' ', '')
sp = n.split()
print("Seu nome em maiúsculo é {}, em minúsculo {}, tem {} caracteres ao todo e seu primeiro nome possui {} letras".format(ma, mi, len(np),len(sp[0])))
