"""Um professor quer sortear dentre seus 4 alunos a ordem de apresentação de seus trabalhos. 
Faça um programa que leia o nome dos alunos e mostre a ordem sorteada"""

from random import sample, random

# sample retorna uma lista de tamanho k com elementos aleatórios escolhidos
# outra opção é usar o shuffle. No shuffle não é necessário determinar a quantidade da amostragem (igual no sample)
a1 = input("Digite nome do aluno: ")
a2 = input("Digite nome do aluno: ")
a3 = input("Digite nome do aluno: ")
a4 = input("Digite nome do aluno: ")
l = [a1, a2, a3, a4]

#eu sei que dá para fazer em loop, com o append para adicionar os elementos na lista. Pesquisar como.

print("A ordem sorteada foi {}.".format(sample(l, k=4)))
