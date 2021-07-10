from matplotlib import pyplot as plt
import csv

def obterDados():
    with open(".\CarRentalData.csv") as f:
        return [dado_carro for dado_carro in csv.DictReader(f)]

def contar_carros_eletricos_por_ano(dados):
    contador = {}

    for carro in dados:
        if carro['fuelType'] == 'ELECTRIC':
            ano = carro['vehicle.year']
            qtd = contador.get(ano, 0) + 1
            contador.update({ano: qtd})
    return contador

def pegar_dados_de_lista_de_tuplas(lista_de_dados, posicao):
    valores = []
    for valor in lista_de_dados:
        valores.append(valor[posicao])
    return valores

#le os dados do CSV
dados_carros = obterDados()

#conta os carros por ano
carros_eletricos_por_ano = contar_carros_eletricos_por_ano(dados_carros)

#ordena a listagem para o gráfico
carros_ordenados = sorted(carros_eletricos_por_ano.items())

#separação dos dados
anos = pegar_dados_de_lista_de_tuplas(carros_ordenados, 0)
quantidades = pegar_dados_de_lista_de_tuplas(carros_ordenados, 1)

#constroi o grafico
plt.xlabel('Anos')
plt.ylabel('Quantidade de Veículos Elétricos')
plt.plot(anos, quantidades)
plt.show()