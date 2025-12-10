def hi_ha_duplicats(llista):
    vistos = set()
    for element in llista:
        if element in vistos:
            return True  
        vistos.add(element)
    return False  

# Programa principal
print(hi_ha_duplicats([1, 2, 3, 4]))       
print(hi_ha_duplicats([1, 2, 3, 2]))       
print(hi_ha_duplicats(["a", "b", "c", "a"])) 
