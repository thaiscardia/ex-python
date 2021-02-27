from matplotlib import pyplot as plt
import csv

#matplotlib é uma biblioteca EXCLUSIVA para geração de gráficos

def carregarArquivo(arquivo):
    return open(arquivo, newline="") #a função open permite abrir arquivos dentro do python, e o newline com a string vazia informa que não há separador especial de uma linha pra outra

"""def obterDados(arquivo): #precisamos extrair os dados do arquivo... 
    leitor = csv.DictReader(arquivo, delimiter=',') #dictreader faz a leitura dos arquivos e agrupa em dicionários
    return leitor 
    arquivo_csv = carregarArquivo('Outros\depression-dataset\data\scores.csv')
dados = obterDados(arquivo_csv)
print(next(dados)) 
as classes implementadas em python podem implementar um metodo chamado __next__ para suportar esta função next(). Ou seja, o jeito recomendado para acessar o próximo item é chamando next(iterador)
- - - Essa é uma forma de fazer. Hoje eu vi outra e então estou fazendo o update. Mas como é bom ter o conhecimento, fica as duas no código. #hatersgonnahate"""

def obterDados(): #vamos utilizar um gerenciador de contexto, que deixa o arquivo aberto somente no bloco.
    with open("Outros\depression-dataset\data\scores.csv") as f:
        return [genderData for genderData in csv.DictReader(f)] #estamos utilizando aqui um list comprehension

def genCounterPerAgeGap(data):
    counterF = {}
    counterM = {}

    for gen in data:
        if gen['gender'] == '1':
            idadeF = gen['age']
            qtdF = counterF.get(idadeF, 0) + 1
            counterF.update({idadeF: qtdF})
            print(counterF)
        else:
            idadeM = gen['age']
            qtdM = counterM.get(idadeM, 0) + 1
            counterM.update({idadeM: qtdM})

    return counterF, counterM

dados = obterDados()
genCounterPerAgeGap(dados)