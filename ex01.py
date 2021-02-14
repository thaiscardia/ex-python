

print('\033[7;30;44mHello, World! 🌍 \033[m') #emoji inserido com botão windows + .

nome = input("Escreva seu nome: ") #pega o dado do user
print("É um prazer te conhecer, {}!".format(nome)) #format substitui o {} com a variável informada

print("Vamos fazer uma validação de string...")
algo = input("Digite algo: ") #input é SEMPRE string. Para fazer este teste é necessário fazer a conversão
print("O tipo primitivo deste valor é", type(algo))
print("Só tem espaços?", algo.isspace())
print("É um número?", algo.isnumeric())
print("É alfabético?", algo.isalpha())
print("É alfanumérico?", algo.isalnum())
print("Está somente em maiúscula?", algo.isupper())
print("Está somente em minúscula?", algo.islower())
print("Está Capitalizada?", algo.istitle())

#para receber um numero no input
print("Vamos somar dois números?")
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = n1 + n2
print("A soma é {}".format(n3))


"""ordem de precedencia:
1 - () | 2 - ** | 3 - * / // % | 4- + -

"""
