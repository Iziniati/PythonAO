def crear_llista_fitxer(nom_fitxer):
    llista_paraules = []
    try:
        with open(nom_fitxer, "r", encoding="utf-8") as fitxer:
            for linia in fitxer:
                paraules = linia.split()
                llista_paraules.extend(paraules)
    except FileNotFoundError:
        print(f"No s'ha trobat el fitxer {nom_fitxer}.")
    return llista_paraules

# Programa principal
nom_fitxer = "exemple.txt" 
llista = crear_llista_fitxer(nom_fitxer)
print("Llista de paraules:", llista)
