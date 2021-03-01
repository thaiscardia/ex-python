import matplotlib.pyplot as plt
import csv

def obterDados():
    with open("scores.csv") as f:
        return [dados_dep for dados_dep in csv.DictReader(f)]

def contagem_mulheres(dados):
    contador_feminino = {}
    for genero in dados:
        if genero['gender'] == '1':
            idade = genero['age']
            qtd = contador_feminino.get(idade, 0) + 1
            contador_feminino.update({idade: qtd})
    return contador_feminino

def contagem_homens(dados):
    contador_masculino = {}
    for homem in dados:
        if homem['gender'] == '2':
            age = homem['age']
            qtt = contador_masculino.get(age, 0) + 1
            contador_masculino.update({age: qtt})
    return contador_masculino

def tupla_feminina(lis_fem, position):
    val = []
    for value in lis_fem:
        val.append(value[position])
    return val

def tupla_masculina(lis_mas, posicao):
    
    valor = []
    for i in lis_mas:
        valor.append(i[posicao])
    return valor

#puxar os dados
dep = obterDados()

#contar a quantidade de individuos
qtdMulherporIdade = contagem_mulheres(dep)
qtdHomporIdade = contagem_homens(dep)

#organização dos dados
x = sorted(qtdMulherporIdade.items()) #dados femininos organizados
counts = sorted(qtdHomporIdade.items()) #dados masculinos organizados

#separação dos dados femininos
anos = tupla_feminina(x, 0)
quantidades = tupla_feminina(x, 1)
print(anos)
#separação dos dados masculinos
anoM = tupla_masculina(counts, 0)
quantidadeM = tupla_masculina(counts, 1)
print(quantidadeM)

#constrói o gráfico
average_age = quantidadeM
bins = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
plt.hist(average_age, bins, histtype='bar', rwidth=100)
plt.xlabel("Idade")
plt.ylabel("Quantidade de indivíduos")
plt.show()
