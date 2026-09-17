def soma_numeros (num1, num2): # num1 e num2 são os parametros que a função recebe
    soma = num1 + num2
    return soma

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))
numero4 = float(input("Digite o quarto numero: "))
numero5 = float(input("Digite o quinto numero: "))
numero6 = float(input("Digite o sexto numero: "))


print("A soma do primeiro par é:",soma_numeros(numero1, numero2)) #função é chamada e as variaveis são os parametros que serão utilizados pela função
print("A soma do segundo par é:",soma_numeros(numero3, numero4))
print("A soma do terceiro par é:",soma_numeros(numero5, numero6))