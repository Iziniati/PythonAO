
while True:
    capital = float(input("Introdueix la quantitat a sol·licitar (50.000€ - 800.000€): "))
    if 50000 <= capital <= 800000:
        break
    print("Error: La quantitat ha d'estar entre 50.000€ i 800.000€.")

while True:
    interes = float(input("Introdueix l'interès (%) (0.5 - 13): "))
    if 0.5 <= interes <= 13:
        break
    print("Error: L'interès ha d'estar entre 0.5% i 13%.")

while True:
    anys = int(input("Introdueix el número d'anys (3 - 40): "))
    if 3 <= anys <= 40:
        break
    print("Error: Els anys han d'estar entre 3 i 40.")

Cfinal = capital * (1 + interes / 100) ** anys

print(f"\nEl capital final després de {anys} anys serà: {Cfinal:.2f} €")
