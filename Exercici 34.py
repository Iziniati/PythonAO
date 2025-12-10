def nums_que_comencen_per(llista_noms, lletra):
    comptador = 0

    for nom in llista_noms:
        if nom.lower().startswith(lletra.lower()):
            comptador = comptador + 1

    return comptador


# Programa principal
noms = ["Anna", "Pau", "Aina", "Joan", "albert", "Maria"]

lletra_usuari = input("Introdueix una lletra: ")

print("Noms que comencen per", lletra_usuari + ":")
print(nums_que_comencen_per(noms, lletra_usuari))
