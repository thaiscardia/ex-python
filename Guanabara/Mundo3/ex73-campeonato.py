""" Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem da colocação. 
Depois mostre: 
a) apenas os 5 primeiros colocados.
B) os últimos 4 colocados da tabela. 
c) uma lista com os times em ordem alfabética.
d) em que posição na tabela está o time chapecoense.
"""

tupla = ("Palmeiras", "Atlético-MG", "Fortaleza", "Red Bull Bragantino", "Athletico", "Flamengo", "Ceará", "Bahia", "Fluminense", "Santos", "Atletico-GO", "Corinthians", "Internacional", "Juventude", "Cuiabá", "São Paulo", "Sport", "América-MG", "Grêmio", "Chapecoense")


print(f"Chapecoense encontra-se na posição {tupla.index('Chapecoense')}")
print(f"Os cinco primeiros colocados são {tupla[0:5]}")
print(f"Os últimos colocados são {tupla[-4:]}")
print(f'Em ordem alfabética: {sorted(tupla)}')
