# -*- coding: utf-8 -*-
# Programa: invertenum1.py
# Programador:
# Data: 26/03/2010
# Este programa que lê um número inteiro de quatro dígitos 
# num = d_3d_2d_1d_0 onde 0 indica a posição das unidades, 1 a das 
# dezenas, 2 a das centenas e 3 a dos milhares
# (num =  d_2*10^2 + d_1*10^1 + d_0*10^0).
# O seu programa deve inverter a ordem dos dígitos de num e gerar o
# numinvertido = d_0d_1d_2d_3 e imprimir o resultado.

# início

# pré: num && num == d[3]d[2]d[1]d[0]

# Passo 1. Leia os números
num = int(input())

d0 = num // 1000
d1 = (num // 100) % 10
d2 = (num // 10) % 10
d3 = num % 10

numinv = d0 + d1*10 + d2*100 + d3*1000


# Passo 3. Imprima o número invertido
print('{0:d}'.format(numinv))

# pós: numinv == dig[0]dig[1]dig[2]dig[3]