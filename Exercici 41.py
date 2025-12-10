while True:
    numero = int(input("Introdueix un número menor de 100: "))
    if numero < 100:
        break
    print("El número ha de ser menor de 100.")

suma = 0
for n in range(numero, 0, -4):
    suma += n**2

print(f"La suma dels quadrats separats 4 posicions és: {suma}")
