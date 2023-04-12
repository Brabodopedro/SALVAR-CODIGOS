# -*- coding: utf-8 -*-
# Programa: somasequencia00.py
# Programador:
# Data: 12/09/2016
# Este algoritmo calcula a soma da sequencia
# S = inicio + (inicio + 1) .... + fim
# início do módulo principal
# descrição das variáveis utilizadas
# int inicio, fim soma

# pré: inicio fim

# Passo 1. Leia o início e fim da sequência
inicio = int(input())
fim = int(input())
# Passo 2. Calcule a soma dos numtermos da sequência
soma = 0
i = inicio

while i < fim +1:
    soma = soma + i
    i = i + 1
# Passo 3. Imprima o valor da soma
print('{0:d}'.format(soma))

# pós: soma == Soma i em {inicio,...,fim}:i 
# fim do módulo principal