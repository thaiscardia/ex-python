num1 = int(input("Insira primeiro número: "))
num2 = int(input("Insira segundo número: "))

if num1 > num2:
    print("O primeiro valor inserido, número {}, é maior".format(num1))
elif num2 > num1:
    print("O segundo valor inserido, número {}, é maior".format(num2))
else:
    print("Os números são de mesmo valor")