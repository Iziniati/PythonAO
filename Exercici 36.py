def es_de_traspas(any):
    if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
        return True
    else:
        return False

# Programa principal
print(es_de_traspas(2020))  
print(es_de_traspas(1900))  
print(es_de_traspas(2000))  
print(es_de_traspas(2021))  
