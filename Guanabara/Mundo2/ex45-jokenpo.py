"""Crie um programa que faça o computador jogar jokenpô com você"""
esc = int(input("Vamos brincar de Jokenpô! Escolha: \n [1] para Pedra \n [2] para Papel \n [3] para Tesoura \n Sua escolha: "))

from random import randint
comp = randint(1,3)
print("Minha escolha é {}.".format(comp))

if esc == 1 and comp == 1 or esc == 2 and comp == 2 or esc == 3 and comp == 3:
    print("Empate! Jogue novamente.".format(esc, comp))
elif esc == 1 and comp == 3 or esc == 2 and comp == 1:
    print("Parabéns, você GANHOU!")
elif esc == 3 and comp == 1 or esc == 2 and comp == 3:
    print("Você PERDEU! Tente novamente!")
else: print("Escolha um número adequado.")