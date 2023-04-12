# -*- coding: utf-8 -*-
# Programa: primeiroultimo.py
# Programador:
# Data: 03/05/2016
# Este programa lê um número inteiro e computa se o primeiro e o
# último número são iguais.
# início do módulo principal
# descrição das variáveis utilizadas
# int numero, ultimo, primeiro, digito
# str msg

# pré: numero

# Passo 1. Leia um número inteiro
numero = int(input())
# Passo 2. Verifique se o primeiro e o último dígito são iguais 
# Passo 2.1. Compute o último dígito
ultimo = numero%10
# Passo 2.2. Retire os digitos internos de numero
msg = str
# fim while
# Passo 2.3. Compute o primeiro digito
posi = numero

while 10 < posi :
    posi = posi//10

# Passo 2.4. Verifique se ultimo e igual a primeiro
if posi == ultimo :
    msg = "sim"
else:
    msg = "nao"
# Passo 3. Imprima o resultado

print(msg)
# pós: 'sim' and numero[0] == numero[n-1] or 'não'
# fim do módulo principal

