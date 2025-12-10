def llista_a_diccionari(llista):
    return {element: i for i, element in enumerate(llista)}
# Programa principal
llista = ['casa', 'cotxe', 'cadira', 'taula']
diccionari = llista_a_diccionari(llista)
print(diccionari)

