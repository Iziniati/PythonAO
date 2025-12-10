any_actual = int(input("Introdueix l'any actual: "))

noms = []
naixements = []

for i in range(4):
    nom = input("Nom de la persona: ")
    any_naixement = int(input("Any de naixement: "))
    
    noms.append(nom)
    naixements.append(any_naixement)

print("Nom\t\tData naixement\tAnys que farà aquest any")

for i in range(4):
    edat = any_actual - naixements[i]
    print(noms[i], "\t\t", naixements[i], "\t\t", edat)
