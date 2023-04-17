num = int(input("Digite um número inteiro positivo: "))

# inicializa a variável contadora com zero
cont = 0

# enquanto o número for maior que zero, incrementa a contagem e divide o número por 10
while num > 0:
    cont += 1
    num //= 10  # operador "//" retorna a parte inteira da divisão

# exibe o resultado
print("O número digitado possui", cont, "dígito(s).")
# -*- coding: utf-8 -*-
# Programa: tamanho.py
# Programador:
# Data: 03/05/2010
# Este programa le um numero inteiro indicando a quantidade 
# de numeros a serem lidos. O programa le cada um dos numeros
# e a cada numero lido computa a quantidade de digitos do 
# numero.
# inicio do módulo principal
# descrição das variáveis utilizadas
# int numero
# int num, digitos 

# pré: numero

# Passo 1. Leia um numero
numero = int(input)
# Passo 2. Compute o numero de digitos
# Passo 2.1. Incialize o numero de digitos

while num > 0:
    cont += 1
    num //= 10

# Passo 2.4. Imprime o resultado
print('{0:d}'.format(digitos))

# pos: digitos == n
# fim do módulo principal
