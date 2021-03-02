import matplotlib.pyplot as plt
bins = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
teste = [2, 4, 2, 4, 5, 3, 4, 1]
plt.hist(teste, bins, histtype='bar', rwidth=0.9)
plt.xlabel("Idade")
plt.ylabel("Quantidade de indivíduos")
plt.show()