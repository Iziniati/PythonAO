def crear_punts(llista):
    for numero in llista:
        línia = ""
        for i in range(numero):
            línia = línia + "."
        print(línia)


# Programa principal
crear_punts([5, 8, 12])

