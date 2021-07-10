#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print("Vamos fazer um financiamento? Por favor informe os valores abaixo para cálculo:")
casa = float(input("Digite o valor do imóvel: R$"))
sal = float(input("E qual é seu salário? R$"))
anos = int(input("E em quantos anos deseja quitar? "))

conv = anos * 12
calc = casa / conv
per = sal * 30 / 100
dif = sal - per
salA = sal - dif
if calc > salA:
    print("Desculpe, seu empréstimo foi \033[31mNEGADO\033[m, pois o valor é 30% \033[31mMAIOR\033[m que seu salário - Prestações de R${:.2f}".format(calc))
else:
    print("Seu empréstimo foi \033[0;30;32mAPROVADO\033[m!!. Suas prestações serão de R${:.2f}".format(calc))
