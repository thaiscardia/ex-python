
#Escreva um programa que converta uma temperatura digitada em ºC e a converta para ºF
tC = float(input("Qual a temperatura em ºC? "))
F = (tC * 9/5) + 32

print("A temperatura de {}ºC corresponde a {}ºF.".format(tC, F))