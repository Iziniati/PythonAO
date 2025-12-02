def es_palindrom(paraula):
    paraula = paraula.lower()

    invertida = ""
    for lletra in paraula:
        invertida = lletra + invertida

    if paraula == invertida:
        return True
    else:
        return False


# Programa principal
print(es_palindrom("radar"))   
print(es_palindrom("civic"))   
print(es_palindrom("hola"))    
