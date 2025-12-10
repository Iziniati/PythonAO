while True:
    numero = int(input("Introdueix un número entre 1 i 20: "))
    if 1 <= numero <= 20:
        break
    print("Error: el número ha d'estar entre 1 i 20.")

print(f"\nTaula de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
