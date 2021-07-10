"""definir o limite para 1000
%5 == 0 -> uma função or %3 == 0
se o num for divisivel, lista;
soma a lista
"""


def calculo():
    lista = []
    
    for num in range(1, 1000):
        if num %5 == 0 or num %3 == 0:
            lista.append(num)
            
    soma = sum(lista)
    print(soma)
calculo()