#Aquest me ha ajudat chat gpt
def crear_punts(llista):
    for numero in llista:
        print("." * numero)

def dibuixar_diamant(alçada):
    llista = []

    for i in range(1, alçada * 2, 2):
        llista.append(i)
    
    for i in range(alçada * 2 - 3, 0, -2):
        llista.append(i)

    for numero in llista:
        espais = (alçada * 2 - 1 - numero) // 2
        print(" " * espais + "." * numero)

# Programa principal
dibuixar_diamant(5)



"""
# Aquest l'he fet jo

def crear_punts(llista):
    for numero in llista:
        print("." * numero)

def dibuixar_imatge():
    crear_punts([1, 3, 5, 3, 1])

# Programa principal
dibuixar_imatge()
"""