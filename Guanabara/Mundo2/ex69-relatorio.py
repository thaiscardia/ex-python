""" Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá pergutar se o usuário quer ou não continuar. 
No final, mostre: a) quantas pessoas tem mais de 18 anos b) quantos homens foram cadastrados c) quantas mulheres com menos de 20 anos
"""
contadorIdade = menor = homem = 0

while True:
    sexo = ' '
    idade = int(input("Informe a idade: "))
    
    while sexo not in "MF":
        sexo = str(input("Insira o sexo: \n [F] para Feminino \n [M] para Masculino \n")).upper().strip()[0]
    
    if idade >= 18: contadorIdade += 1
    
    if sexo == "M": homem += 1
    
    if sexo == "F" and idade < 20: menor += 1
    
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input("Você deseja continuar? \n [S] SIM \n [N] NÃO \n")).strip().upper()[0]
    if continuar == "N":
        break
        
print(f"Há um total de {contadorIdade} pessoas acima de 18 anos")
print(f"Foram cadastrados {homem} homens")
print(f"Ao todo são {menor} mulheres com menos de 20 anos.")

