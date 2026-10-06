# 🔢 Números Pares e Ímpares em Python

Programa desenvolvido em Python para praticar **listas, estruturas de repetição, condicionais e contadores**, identificando números pares e ímpares.

## 📖 Sobre

O objetivo deste projeto é colocar em prática conceitos de lógica de programação utilizando uma lista de números.

O programa permite cadastrar **8 números**, exibir os números cadastrados, identificar quais são pares e ímpares e, ao final, informar a quantidade de cada tipo.

## ✨ Funcionalidades

* 🔢 Cadastro de 8 números
* 📋 Exibição dos números cadastrados
* 🟢 Identificação dos números pares
* 🟠 Identificação dos números ímpares
* 🔢 Contagem de números pares
* 🔢 Contagem de números ímpares

## 🧠 Conceitos praticados

Neste projeto foram utilizados:

* Listas (`list`)
* `for`
* `range()`
* `input()`
* `int()`
* `append()`
* Operador módulo (`%`)
* Estrutura condicional `if/else`
* Operadores de comparação
* Variáveis contadoras
* Operador `+=`
* `print()`

## 💻 Como funciona

Primeiro, o programa cria uma lista vazia:

```python
numeros = []
```

Em seguida, utiliza um `for` com `range(8)` para solicitar 8 números ao usuário e armazená-los na lista:

```python
for i in range(8):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
```

Depois, o programa percorre a lista e verifica quais números são pares.

Para descobrir se um número é par, é utilizado o operador `%`:

```python
if numero % 2 == 0:
    print("Os números pares são: ", numero)
```

Também é feita uma verificação separada para identificar os números ímpares:

```python
if numero % 2 != 0:
    print("Os ímpares são: ", numero)
```

Por fim, são utilizados dois contadores para descobrir quantos números pares e ímpares existem na lista:

```python
contador_pares = 0
contador_impares = 0
```

A cada número encontrado, o contador correspondente é incrementado:

```python
contador_pares += 1
```

ou:

```python
contador_impares += 1
```

## 📌 Exemplo de execução

```text
Digite um número: 10
Digite um número: 3
Digite um número: 8
Digite um número: 7
Digite um número: 4
Digite um número: 11
Digite um número: 2
Digite um número: 5

Os números cadastrados são: 10
Os números pares são: 10
Os números cadastrados são: 3
Os números cadastrados são: 8
Os números pares são: 8
Os números cadastrados são: 7
Os números cadastrados são: 4
Os números pares são: 4
Os números cadastrados são: 11
Os números cadastrados são: 2
Os números pares são: 2
Os números cadastrados são: 5

Os ímpares são: 3
Os ímpares são: 7
Os ímpares são: 11
Os ímpares são: 5

Quantidade de pares: 4
Quantidade de ímpares: 4
```

## 🎯 Objetivo do projeto

Este projeto faz parte dos meus estudos de **Python e lógica de programação**.

O exercício foi desenvolvido para praticar o uso de listas, estruturas de repetição e condições, além de aprender a utilizar **contadores para armazenar a quantidade de elementos que atendem a determinada condição**.

## 🛠 Tecnologias

* Python
* Git
* GitHub

## 👨‍💻 Autor

**Felipe Oliveira**

GitHub:
https://github.com/oliveiracfelipe
