def comptar_majuscules(cadena):
    contador = 0
    for lletra in cadena:
        if lletra.isupper():
            contador = contador + 1
    return contador

# Programa principal
print(comptar_majuscules("Hola"))
print(comptar_majuscules("AIXÒ ÉS PROVA")) 
print(comptar_majuscules("python"))        
print(comptar_majuscules("PyThOn"))        
