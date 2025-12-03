def filtrar_paraules(llista_paraules, x):
    paraules_filtrades = []

    for paraula in llista_paraules:
        if len(paraula) > x:
            paraules_filtrades.append(paraula)

    return paraules_filtrades

# Programa principal
llista = ["Hola", "Ramis", "IES", "Paraula", "Python"]
print(filtrar_paraules(llista, 4))  # ['Ramis', 'Paraula', 'Python']
