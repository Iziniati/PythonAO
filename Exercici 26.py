def gran_llista(llista):
    mes_gran = llista[0]

    for numero in llista:
        if numero > mes_gran:
            mes_gran = numero

    return mes_gran

# Programa principal
print(gran_llista([1384, 5532, 2213, 3, 3425]))  
