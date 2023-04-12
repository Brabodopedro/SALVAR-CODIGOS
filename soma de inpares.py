inicio , fim = map(int, input().split())

soma = 0
i = inicio

if inicio%2 == 0:
    i = inicio + 1
    
else:
    i = inicio
    
while i < fim +1:
    soma = soma + i
    i = i + 2
    
print('{0:d}'.format(soma))


    