# escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
d = float(input("Digite a distância em metros: "))
c = d * 100
m = d * 1000
print("A distância informada foi {}. Esta distância em centímetros é {}, e em milímetros é {}.".format(d, c, m))