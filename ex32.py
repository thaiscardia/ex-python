#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

s = float(input("Digite o salário do funcionário: "))
sA = 10
sB = 15

if s >= 1250:
    s += (s * sB) / 100
    print("Seu salário com {}% de aumento é de R${:.2f}". format(sB, s))
else:
    s += (s * sA) / 100
    print("Seu salário com {}% de aumento é de R${:.2f}.".format(sA, s))

