# Pedir 6 números ao usuário.
# Adicionar cada número à lista.
# Mostrar os números na ordem em que foram digitados.
# Ordenar a lista em ordem crescente usando .sort().
# Mostrar a lista ordenada.
# Mostrar quantos números foram cadastrados.
# Perguntar um número ao usuário e verificar se ele está na lista.

numeros = [] # 1 Lista vazia

for i in range(6): # 2 Adicionar os números na lista
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print("=============================")

for numero in numeros: # 3 Mostrar os números que foram armazenados
    print("Os números são: ", numero)

print("=============================")

numeros.sort(reverse=False) # 4 Formatação para número do menor para maior

for numero in numeros: # 5 Mostrar os números formatados em ordem crescente
    print("Os números ordenados são: ", numero)

print("=============================")

print("A quantidade de números cadastrados: ", len(numeros)) # 6 Informar a quantidade de números que foram cadastrados

print("=============================")


numero_busca = int(input("Digite um número para verificar: ")) # 7 Verificação se está na lista

if numero_busca in numeros: # 8 Lógica para verificação
    print("Está na lista!")
else:
    print("Não está na lista!")