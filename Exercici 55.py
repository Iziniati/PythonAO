print("Números parells fins a 100:")
for numero in range(2, 101, 2):
    print(numero, end=", " if numero < 100 else "\n")

# Programa principal
print("Números senars fins a 100:")
for numero in range(1, 101, 2):
    print(numero, end=", " if numero < 100 else "\n")
