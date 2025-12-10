import random
def llista_20_elements():
    llista = []
    for _ in range(20):
        llista.append(random.randint(1, 100))
    return llista

def hi_ha_duplicats(llista):
    vistos = set()
    for element in llista:
        if element in vistos:
            return True
        vistos.add(element)
    return False

# Programa principal
llista_generada = llista_20_elements()
print("Llista generada:", llista_generada)

if hi_ha_duplicats(llista_generada):
    print("Hi ha elements duplicats a la llista.")
else:
    print("No hi ha elements duplicats a la llista.")
