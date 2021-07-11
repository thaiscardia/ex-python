"""Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
- a vista dinheiro/cheque: 10% de desconto
- a vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""

preco = float(input("Insira preço do produto: "))
metodo = int(input("Insira método de pagamento: \n [1] para A VISTA no dinheiro ou cheque: \n [2] para A VISTA no cartão \n [3] para PARCELAMENTO ATÉ 2X no cartão \n [4] para PARCELAMENTO 3x ou mais no cartão (com juros) \n"))
if metodo == 4: qtd = int(input("Insira em até quantas vezes gostaria de parcelar: "))

#descontos
dCash = 10
dCard = 5
juros = 20

#desconto por tipo de pagamento
cheque = (preco * dCash)/100
cartao = (preco * dCard)/100
cartaoParcelado = preco * (juros/100)

if metodo == 1: print("O valor do produto a ser pago, com {}% de desconto é de R${}.".format(dCash, (preco - cheque)))
elif metodo == 2: print("O valor do produto a ser pago, com {}% de desconto é de R${}.".format(dCard, (preco - cartao)))
elif metodo == 3: print("O valor do produto a ser pago é de R${}.".format(preco))
elif metodo == 4 and qtd >= 3:
    print("O valor do produto a ser pago, com {}% de juros é de R${}.".format(juros, (preco + (cartaoParcelado * qtd))))
else: print("Por gentileza escolha um método válido.")