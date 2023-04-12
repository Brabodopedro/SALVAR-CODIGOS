# -*- coding: utf-8 -*-
# Programa: contachar2.py
# Programador:
# Data: 15/11/2016
# Este programa lê uma palavra e um caractere e conta o 
# número de ocorrências do caractere (independente se for maiúsculo
# ou minúsculo) na palavra e imprime o resultado. 
# início do módulo principal
# descrição das variáveis utilizadas
# int numero
# str palavra, caractere

# pré: palavra caractere

# Passo 1. Leia a palavra e o caractere
# Passo 1.1. Leia uma palavra
print('Leia uma palavra: ')
palavra = str(input())
# Passo 1.2. Leia o caractere
print('Leia um caractere: ')
caractere = str(input())
# Passo 1.3. Inicialize o número de caracteres
contador = 0
for letra in palavra:
    if letra.lower() == caractere.lower():
        contador += 1

print('{0:d}'.format(contador))

# pós: número == Soma letra em palavra: letra == caractere
# fim do módulo principal
