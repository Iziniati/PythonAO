from functools import reduce

def Passar_a_Numero(llista):
    return reduce(lambda x, y: x * 10 + y, llista)

# Programa principal
digits = [3, 4, 1, 5]
numero = Passar_a_Numero(digits)
print(numero)
