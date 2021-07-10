#jogo da adivinhação: tente adivinhar o mesmo número que o computador "pensou"
print( "=" * 20)
print("Vou pensar em um número inteiro entre 0 e 5... ")
print("=" * 20)

from random import randint
from time import sleep #faz o computador "dormir" por tempo determinado

print("Hm...")
sleep(2) #timer em segundos para o "pause" do sistema

def adivinha():
    n = int(input("Que número pensei? "))
    p = randint(0, 5)
    if n == p:
        print("Parabéns, você acertou!")
    else:
        print("Não foi dessa vez. Eu pensei em {}. Tente novamente!".format(p))

adivinha()

