"""Faça um programa que jogue par ou impar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

contador = 0

while True:
        
        numero = int(input("Insira um número: "))
        pc = randint(0, 10)
        resultado = pc + numero
        
        jogo = ' '
        
        while jogo not in "PI":
                jogo = str(input("Vamos jogar Par ou Ímpar? Escolha: [P] Par ou [I] Impar \n")).strip().upper()[0]
        print(f"Você jogou {numero} e o computador {pc}, totalizando em {resultado}")
        
        if jogo == "P":
                if resultado % 2 == 0:
                        print("Parabéns, você VENCEU!!")
                        contador += 1
                else:
                        print("você PERDEU!")
                        break   
        elif jogo == "I":
                if resultado % 3 == 1:
                        print("Parabéns, você VENCEU!!")
                        contador += 1
                else:
                        print("você PERDEU!")
                        break
        print("Vamos jogar novamente...")
print(f"GAME OVER. Você venceu {contador} vezes.")
