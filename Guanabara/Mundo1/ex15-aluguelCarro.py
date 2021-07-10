"""Escreva um programa que pergunte a qtd de km percorridos por um carro alugado e a qtd de dias pelos quais
ele foi alugado, Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado."""
kmR = float(input("Insira a quantidade de Km percorridos: "))
qtdDias = int(input("Insira quantos dias o automóvel foi alugado: "))
vDia = 60
vKm = 0.15

custoDia = qtdDias * vDia
custoRodado = kmR * vKm
custoTotal = custoDia + custoRodado

print("O valor devedor é de R${:.2f}.".format(custoTotal))