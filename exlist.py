numeros = []

for i in range(8):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for numero in numeros:
    print("Os números cadastrados são:", numero)

    if numero % 2 == 0:
        print("Os números pares são: ", numero)

for numero in numeros:
    if numero % 2 != 0:
        print("Os ímpares são: ", numero)

contador_pares = 0
contador_impares = 0

for numero in numeros:
    print("Número:", numero)

    if numero % 2 == 0:
        print("É par!")
        contador_pares += 1

    else:
        print("É ímpar!")
        contador_impares += 1

print("Quantidade de pares:", contador_pares)
print("Quantidade de ímpares:", contador_impares)
