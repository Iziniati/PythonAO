def paraules_per_lletra(llista_paraules, lletra):
    return list(filter(lambda p: p.lower().startswith(lletra.lower()), llista_paraules))

# Programa principal
llista = ["Izan", "Peu", "cama", "Pata"]
resultat = paraules_per_lletra(llista, "p")
print(resultat)
