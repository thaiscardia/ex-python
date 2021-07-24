"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

lista = []

while True:
    
    n = int(input("Insira um número: "))
    c = str(input("Quer continuar? \n [S] SIM \n [N] NÃO \n")).upper().strip()[0]
    if c == "N": break
    
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso.")
    else: print("Valor duplicado. Não adicionado")
print(sorted(lista))