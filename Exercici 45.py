numero = int(input("Introdueix un número: "))

suma_digits = 0
for digit in str(numero):
    suma_digits += int(digit)

if suma_digits % 2 == 0:
    print(f"La suma dels dígits ({suma_digits}) és parell.")
else:
    print(f"La suma dels dígits ({suma_digits}) és senar.")
