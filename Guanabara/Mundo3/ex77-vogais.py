"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
"""

tupla = ("crie", "um", "programa", "que", "tenha", "uma", "tupla", "com", "depois", "disso", "deve", "mostrar", "para", "cada", "palavra", "quais", "suas", "vogais")
vogais = []

for i in tupla:
    print(f'\n Na palavra {i.upper()} temos ', end='')
    for l in i:
        if l in 'aeiou':
            print(f'{l.upper()}', end=' ')