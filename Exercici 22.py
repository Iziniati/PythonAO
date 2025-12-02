def superposicio(llista1, llista2):
    for elem1 in llista1:
        for elem2 in llista2:
            if elem1 == elem2:
                return True
    return False


# Programa principal
print(superposicio([1, 2, 3], [3, 4, 5]))  
print(superposicio([1, 2, 3], [4, 5, 6]))   
