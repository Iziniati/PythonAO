def lenp(frase):
    longituds = list(map(len, frase.split()))
    return longituds

# Programa principal
frase = "Hola Joan, com estas?"
print(lenp(frase))
