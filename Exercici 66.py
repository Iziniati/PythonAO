def coincidencia_valor_index(llista):
    comptador = 0
    for i, valor in enumerate(llista):
        if i == valor:
            comptador += 1
    return comptador

# Programa principal
llista = [0, 2, 3, 3, 4]
resultat = coincidencia_valor_index(llista)
print(resultat)
