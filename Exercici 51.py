def elimina_duplicats(llista):
    nova_llista = []
    for element in llista:
        if element not in nova_llista:
            nova_llista.append(element)
    return nova_llista

# Programa principal
llista_original = [1, 2, 3, 2, 4, 3, 5]
llista_sense_duplicats = elimina_duplicats(llista_original)

print("Llista original:", llista_original)
print("Llista sense duplicats:", llista_sense_duplicats)
