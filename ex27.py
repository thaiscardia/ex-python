#Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

def multa():
    v = int(input("Qual sua velocidade em km/h? "))
    r = 80

    if v <= r:
        print("Você está dentro do limite de velocidade. Continue assim.")
    else:
        ex = v - r
        calc = ex * 7
        print("Você foi multado! O valor que deve pagar é de R${}.".format(calc))

multa()

