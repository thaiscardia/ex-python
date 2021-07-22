"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. 
"""

from random import randint

num = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f"Os números gerados foram {num}")
print(f"O maior número gerado foi {max(num)} e o menor número gerado foi {min(num)}")