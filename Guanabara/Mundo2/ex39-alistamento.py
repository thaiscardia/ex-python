"""Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
- Se ele ainda vai se alistar no serviço militar
- Se é a hora de se alistar
- se já passou do tempo do alistamento
O programa também deverá indicar o tempo que falta ou que passou do prazo"""

from datetime import datetime
nasc = int(input("Insira seu ano de nascimento: "))
now = datetime.now()
idade = now.year - nasc
if idade < 18 or idade <= 17:
    dif = idade - 18
    print ("Você tem {} anos e ainda precisa aguardar {} ano(s) para o alistamento".format(idade, -dif))
elif idade > 18 or idade >= 19: 
    dif = idade - 18
    print ("Você tem {} anos e já passou {} anos do alistamento".format(idade, dif))
elif idade == 18:
    print ("Você está no período do alistamento.")