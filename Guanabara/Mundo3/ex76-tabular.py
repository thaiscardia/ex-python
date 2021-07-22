"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados de forma tabular. 
"""

tupla = ("Lapis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print("-"*30)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-"*30)

for posicao in range(0, len(tupla)):
    if posicao % 2 == 0:
        print(f"{tupla[posicao]:.<30}", end='')
    else:
        print(f"R${tupla[posicao]:>7.2f}")
print("-"*30)