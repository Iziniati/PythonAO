def nums_que_comencen_per(llista_noms):
    comptador = 0

    for nom in llista_noms:
        if nom.lower().startswith("a"): 
            comptador = comptador + 1

    return comptador

# Programa principal
noms = ["Anna", "Pau", "Aina", "Joan", "albert"]
print(nums_que_comencen_per(noms))  
