def concatena_llistes(llista1, llista2, connector):
    return [a + connector + b for a, b in zip(llista1, llista2)]

# Programa principal
llista1 = ["sub", "supra"]
llista2 = ["campió", "campiona"]
resultat = concatena_llistes(llista1, llista2, "-")
print(resultat)
