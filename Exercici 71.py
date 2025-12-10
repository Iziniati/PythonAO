def llegir_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, "r", encoding="utf-8") as fitxer:
            contingut = fitxer.read()
            return contingut
    except FileNotFoundError:
        print(f"Error: el fitxer '{nom_fitxer}' no existeix.")
        return None
    except IOError:
        print(f"Error: hi ha hagut un problema obrint el fitxer '{nom_fitxer}'.")
        return None

# Programa principal
nom = "exemple.txt"
dades = llegir_fitxer(nom)
if dades is not None:
    print("Contingut del fitxer:")
    print(dades)
