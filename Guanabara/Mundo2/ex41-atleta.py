"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: junior
- até 20 anos: sênior
- acima: master"""

from datetime import datetime
nasc = int(input("Insira ano de nascimento: "))
data = datetime.now()
idade = data.year - nasc

if idade <= 9: print("MIRIM")
elif idade == 10 or idade <= 14: print("INFANTIL")
elif idade == 15 or idade <= 19: print("JUNIOR") 
elif idade == 20: print("SENIOR")
else: print("MASTER") 
