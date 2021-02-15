"""Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido."""
from random import choice, random

a1 = input("Digite nome do aluno: ")
a2 = input("Digite nome do aluno: ")
a3 = input("Digite nome do aluno: ")
a4 = input("Digite nome do aluno: ")
l = [a1, a2, a3, a4]

#eu sei que dá para fazer em loop, com o append para adicionar os elementos na lista. Pesquisar como.

print("O aluno escolhido foi {}.".format(choice(l)))