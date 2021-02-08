"""Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido."""
from random import choice

def adicionar():
    nome = print(input("Digite nome do aluno: "))
    conf = print(input("Adicionar outro aluno? "))
    lista = [] 
    sim = True

    while conf == sim:
        lista.append(nome)
        print(nome)
    else:
        print("O aluno escolhido é: ", choice(lista))

adicionar()