def paraula_mes_llarga(llista_paraules):
    mes_llarga = llista_paraules[0]

    for paraula in llista_paraules:
        if len(paraula) > len(mes_llarga):
            mes_llarga = paraula
    return mes_llarga

# Programa principal
print(paraula_mes_llarga(["Hola", "Ramis", "IES", "Paraula"]))  
