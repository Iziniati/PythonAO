def index_paraula(llista_paraules, paraula):
    for i, p in enumerate(llista_paraules):
        if p == paraula:
            return i
    return -1

# Programa principal
llista = ["Ian", "Jordi", "Izan", "Lucas"]
llista.sort()
print("Llista ordenada:", llista)

print(index_paraula(llista, "Maria"))  
print(index_paraula(llista, "Pau"))
