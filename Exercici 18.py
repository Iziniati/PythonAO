"Definir una funció que agafi un caràcter i retorni vertader si és una vocal i en cas contrari retorni fals. Prova-la amb diferents exemples."

def ex18(c):
    v = "aeiouAEIOUàáèéìíòóùúÀÁÈÉÌÍÒÓÙÚ"
    if c in v:
        return True
    else:
        return False

# Programa principal
c = input("Escriu un caracter per a provar si es vocal o no")
print(ex18(c))
