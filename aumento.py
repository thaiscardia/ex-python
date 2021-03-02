#faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
sal = float(input("Digite o salário atual: "))
perAumento = 15
vAumento = (sal * perAumento)/100
print("O valor do salário com {}% de aumento é de {}".format(perAumento, sal + vAumento))
