def eliminarcapicua(llista):
    if len(llista) <= 2:
        return []
    return llista[1:-1]
llista_original = [10, 20, 30, 40, 50]
nova_llista = eliminarcapicua(llista_original)

# Programa principal
print("Llista original:", llista_original)
print("Llista sense primer i últim element:", nova_llista)
