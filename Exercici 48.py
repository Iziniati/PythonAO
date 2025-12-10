def esta_ordenada(llista):
    if llista == sorted(llista):
        return "Està ordenada de forma ascendent"
    elif llista == sorted(llista, reverse=True):
        return "Està ordenada de forma descendent"
    else:
        return "No està ordenada"

# Programa principal
print(esta_ordenada([3, 2, 1]))   
print(esta_ordenada([4, 5, 6]))  
print(esta_ordenada([1, 3, 2]))   
