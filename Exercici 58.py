def elements_parells(llista_paraules):
    for i in range(len(llista_paraules)):
        if i % 2 == 0:  # 
            print(llista_paraules[i])

# Programa principal
llista = ["Ian", "Pau", "Lucas", "Izan", "Rafa"]
print("Elements en posicions parells:")
elements_parells(llista)
