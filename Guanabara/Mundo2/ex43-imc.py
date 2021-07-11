"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida"""


al = float(input("Insira a altura: "))
pe = float(input("Insira o peso em kgs: "))

imc = pe/(al**2)

if imc <= 18.4: print("Abaixo do peso")
elif imc == 18.5 or imc <= 25: print("peso ideal")
elif imc == 25.1 or imc <= 30: print("sobrepeso")
elif imc == 30.1 or imc <= 40: print("obesidade")
else:
    print("obesidade mórbida.")