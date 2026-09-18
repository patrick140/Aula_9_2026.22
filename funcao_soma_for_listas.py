def soma_numeros (num1, num2):
    soma = num1 + num2
    return soma

lista_numeros = []

for i in range(6):
    numero = float(input(f"Digite o {i+1}° numero: "))#caracter f antes da aspa permite você colocar uma variavel dentro da string
    lista_numeros.append(numero)


print("A soma do primeiro par é: ", soma_numeros(lista_numeros[0], lista_numeros[1]))
print("A soma do segundo par é: ", soma_numeros(lista_numeros[2], lista_numeros[3]))
print("A soma do terceiro par é: ", soma_numeros(lista_numeros[4], lista_numeros[5]))