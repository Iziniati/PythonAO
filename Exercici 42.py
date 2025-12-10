while True:
    numero = int(input("Introdueix un número entre 1 i 900000: "))
    if 1 <= numero <= 900000:
        break
    print("Error: el número ha d'estar entre 1 i 900000.")

quantitat_digits = len(str(numero))

print(f"El número {numero} té {quantitat_digits} dígits.")
