def crear_repetits(num, caracter):
    resultat = ""
    for i in range(num):
        resultat = resultat + caracter
    return resultat

# Programa principal
print(crear_repetits(5, "a"))   

