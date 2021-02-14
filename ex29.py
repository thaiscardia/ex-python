#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

def calc():
    d = int(input("Digite a distância em km: "))
    if d <= 200:
        v = d * 0.50
        print("O valor da passagem será de R${:.2f}".format(v))
    else:
        v = d * 0.45
        print("O valor da passagem será de R${:.2f}.".format(v))

calc()

