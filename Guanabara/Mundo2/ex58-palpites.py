"""Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.  
"""
from random import randint
from time import sleep #faz o computador "dormir" por tempo determinado

def adivinha():
    
    print( "=" * 20)
    print("Vou pensar em um número inteiro entre 0 e 10... ")
    print("=" * 20)
    print("Hm...")
    sleep(2) #timer em segundos para o "pause" do sistema
    
    p = randint(0, 10)
    r = False
    contador = 0
    
    while not r:
        n = int(input("Que número pensei? "))
        contador += 1
        if n == p:
            r = True
        else:
            if n < p:
                print("Errou. Número maior. Tente novamente.")
            elif n > p:
                print("Errou. Número menor. Tente novamente.")        
    print("Parabéns, você acertou após {} tentativas!".format(contador))

adivinha()