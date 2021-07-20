""" Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai ocntinuar. No final, mostre:
a) qual é o total de gasto na compra. b) quantos produtos custam mais de R$1000 c) qual é o nome do produto mais barato.
"""
#REVER EXERCÍCIO

total = acima = menor = contador = cheap = 0

while True:
    produto = str(input("Insira nome do produto: "))
    price = float(input("Insira valor do produto: R$"))
    contador =+ 1
    total += price
    
    if price > 1000:
        acima += 1
    
    if contador == 0:
        menor = price
        cheap = produto
    elif contador == 1 or price < menor:
        menor = price
        cheap = produto
    
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input("Deseja continuar? \n[S] SIM \n [N] NÃO \n")).strip().upper()[0]
    if continuar == "N":
        break

print("Programa Encerrado!")  
print(f"O total gasto na compra é de R${total:.2f}")
print(f"Existem {acima} produtos acima de R$1000")
print(f"O produto de valor mais baixo é o {cheap}")