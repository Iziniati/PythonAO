def gran_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b>= a and b >= c:
        return b
    else:
        return c
    
print("Exemples de prova de la funcio gran_de_tres():")
print("gran_de_tres(5,3,7) =", gran_de_tres(5,3,7))
print("gran_de_tres(100,20,30) =", gran_de_tres(100,20,30))
print("gran_de_tres(21,34,62) =", gran_de_tres(21,34,62))