"""Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-la por extenso
"""

num = int(input("Digite um número de 0 a 20: "))
tupla = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
print("O número digitado foi o número {}".format(tupla[num]))