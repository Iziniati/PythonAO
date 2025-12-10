def dividir(a, b):
    try:
        resultat = a / b
        return resultat
    except ZeroDivisionError:
        return "Error: no es pot dividir per zero!"

# Programa principal
print(dividir(10, 2))  
print(dividir(10, 0))  
