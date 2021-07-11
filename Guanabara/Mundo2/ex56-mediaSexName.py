"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- a média de idade do grupo.
- Qual é o nome do homem mais velho.
- quantas mulheres tem menos de 20 anos
"""

def leitor():
    
    somaIdade = 0
    nomeH = ''
    velhoH = 0
    mulher = 0
    
    for dados in range (1, 5):
        print('----{}ª PESSOA ----'.format(dados))
        
        nome = str(input("Insira o nome: ")).upper()
        sexo = str(input("Insira o sexo: \n [F] para Feminino \n [M] para Masculino \n")).upper()
        idade = int(input("Informe a idade: "))
        somaIdade += idade
        
        if dados == 1 and sexo == "M":
            velhoH = idade
            nomeH = nome
        
        if sexo == "M" and idade > velhoH:
            velhoH = idade
            nomeH = nome
        
        if sexo == "F" and idade < 20:
            mulher += 1
            
    
    media = float(somaIdade/4)
    print("A média de idade do grupo é de {} anos".format(media))
    print("O homem mais velho tem {} anos e se chama {}".format(velhoH, nomeH))
    print("Ao todo são {} mulheres com menos de 20 anos.".format(mulher))

leitor()