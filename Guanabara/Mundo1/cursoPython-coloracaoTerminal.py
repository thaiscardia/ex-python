#para adicionar cores modo ANSI precisa colocar o código \033[INCLUI CODIGOm ou seja \033[0;33;44m | o 0 é opcional (quando não há configuração)
#Sendo categorizada: estilo do texto (0 [sem estilo, 1 [negrito], 4[sublinhado, 7[negativo/inverte]]]), a cor da fonte [de 30 a 37], e as cores de background [de 40 a 47]
#para gerar a cor preta, que é a cor padrão, é só utilizar o código \033[m (desfaz todas as configurações). Exemplo:

nome = input("Digite seu nome: ")
cores = {'limpa': '\033[m', 'branca': '\033[30m', 'vermelha': '\033[31m', 'verde': '\033[32m', 'amarela': '\033[33m', 'azul': '\033[34m', 'roxa': '\033[35m', 'azul turquesa': '\033[36m', 'cinza': '\033[37m'}
print("Olá, {}, veja seu nome colorido: \n{}{} \n{}{} \n{}{}".format(nome, cores['vermelha'], nome, cores['verde'], nome, cores['azul'], nome ))