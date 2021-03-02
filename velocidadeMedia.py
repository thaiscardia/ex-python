#Se você correr 10km em 42min e 42seg, qual é o seu passo médio (tempo por milha em minutos e segundos)?
#Qual a sua velocidade média em milhas por hora? Considere uma milha = 1,61km.

tS = (42 * 60) + 42 #tempo em segundos
dM = 10 * 1.61 #distancia em milhas
tH = (tS / 60) / 60
v = dM / tH
print("Sua velocidade média é {:.2f} milhas/hora".format(v))