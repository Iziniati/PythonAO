def binari_a_enter(binari):
    resultat = 0
    potencia = 0

    for digit in binari[::-1]:
        if digit == "1":
            resultat = resultat + (2 ** potencia)
        potencia = potencia + 1

    return resultat

# Programa principal
print(binari_a_enter("101"))     
print(binari_a_enter("1001"))    
print(binari_a_enter("1111"))    
print(binari_a_enter("0001"))    
