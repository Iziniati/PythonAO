num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))

if num1 > num2:
    num1, num2 = num2, num1

suma = 0
for numero in range(num1, num2 + 1):
    suma += numero

print(f"La suma de tots els números entre {num1} i {num2} és: {suma}")
