from matplotlib import pyplot as plt
import csv

def obterDados(): #vamos utilizar um gerenciador de contexto, que deixa o arquivo aberto somente no bloco.
    with open(".\depression-dataset\data\scores.csv") as f:
        return [genderData for genderData in csv.DictReader(f)] #estamos utilizando aqui um list comprehension

def genFem(data):
    counterF = {}

    for gen in data:
        if gen['gender'] == '1':
            idadeF = gen['age']
            qtdF = counterF.get(idadeF, 0) + 1
            counterF.update({idadeF: qtdF})
    return counterF

def genMale(data):
    counterM = {}
    for gend in data:
        if gend['gender'] == '2':
            idadeM = gend['age']
            qtdM = counterM.get(idadeM, 0) + 1
            counterM.update({idadeM: qtdM})
    return counterM

def tupla_fem(femData, posicao):
    val = []
    for value in femData:
        val.append(value[posicao])
    return val

def tupla_mas(masData, position):
    valu = []
    for quan in masData:
        valu.append(quan[position])
    return valu

dados = obterDados()

feminino = genFem(dados) #contém age gap + qtd
masculino = genMale(dados) #contém age gap + qtd

dados_ordenados_femininos = sorted(genFem.items())
dados_ordenados_masculinos = sorted(genMale.items())

qtdFem = tupla_fem(dados_ordenados_femininos, 0)
qtdMas = tupla_mas(dados_ordenados_masculinos, 0)

ageFem = tupla_fem(dados_ordenados_femininos, 1)
ageMas = tupla_mas(dados_ordenados_masculinos, 1)

plt.plot(qtdFem, ageFem)
plt.plot(qtdMas, ageMas)