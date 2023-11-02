palavra_codificada = str(input())
deslocamento = int(input())

palavra_decodificada = ""

for letra in palavra_codificada:
    codigo = ord(letra)
    codigo_decodificado = codigo - deslocamento
    letra_decodificada = chr(codigo_decodificado)
    palavra_decodificada += letra_decodificada

print(palavra_decodificada)
