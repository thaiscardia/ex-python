"""Faça um programa que leia uma frase pelo teclado e mostre:
- quantas vezes aparece a letra "A";
- em que posição ela aparece a primeira vez;
- em que posição ela aparece a última vez;"""

f = input("Digite a frase aqui: ")
f = f.upper()
print("Esta frase possui {} letra(s) A".format(f.count("A")))
print("O primeiro A da string está localizado em {} e o último em {}.".format(f.index("A"), f.rindex("A")))