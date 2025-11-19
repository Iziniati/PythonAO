def menu_principal():
    opcio = 0
    while opcio < 1 or opcio > 4:
        opcio = int(input("""Eligeix una opció:
        1. Calculadora decimal
        2. Calculadora real (floats)
        3. Sortir
        4. Canvis de base (bin, oct, dec, hex)
        """))
    return opcio


def menu_calculadora():
    opcio = 0
    while opcio < 1 or opcio > 5:
        opcio = int(input("""Eligeix una opció:
        1. Suma
        2. Resta
        3. Multiplicació
        4. Divisió
        5. Sortir
        """))
    return opcio


def calculadora_decimal(opcio):
    if 1 <= opcio <= 4:
        a = int(input("Introdueix el primer nombre: "))
        b = int(input("Introdueix el segon nombre: "))

    match opcio:
        case 1:
            print("Estic fent la suma!\n")
            print(f"El resultat de {a} + {b} és {a + b}")
        case 2:
            print("Estic fent la resta!\n")
            print(f"El resultat de {a} - {b} és {a - b}")
        case 3:
            print("Estic fent la multiplicació!\n")
            print(f"El resultat de {a} * {b} és {a * b}")
        case 4:
            print("Estic fent la divisió!\n")
            print(f"El resultat de {a} / {b} és {a // b}")
        case _:
            print("Opció no vàlida!\n")


def calculadora_real(opcio):
    if 1 <= opcio <= 4:
        a = float(input("Introdueix el primer nombre: "))
        b = float(input("Introdueix el segon nombre: "))

    match opcio:
        case 1:
            print("Estic fent la suma!\n")
            print(f"El resultat de {a} + {b} és {a + b}")
        case 2:
            print("Estic fent la resta!\n")
            print(f"El resultat de {a} - {b} és {a - b}")
        case 3:
            print("Estic fent la multiplicació!\n")
            print(f"El resultat de {a} * {b} és {a * b}")
        case 4:
            print("Estic fent la divisió!\n")
            print(f"El resultat de {a} / {b} és {a / b}")
        case _:
            print("Opció no vàlida!\n")


# ------------------------------
#         CANVIS DE BASE
# ------------------------------

def menu_bases(text):
    opcio = 0
    while opcio < 1 or opcio > 4:
        opcio = int(input(f"""{text}
        1. Binari
        2. Octal
        3. Decimal
        4. Hexadecimal
        """))
    return opcio


def canvi_base():
    print("=== CANVI DE BASE ===")
    origen = menu_bases("Tria la base d'origen:")
    desti = menu_bases("Tria la base de destí:")

    valor = input("Introdueix el nombre en la base seleccionada: ")

    bases = {1: 2, 2: 8, 3: 10, 4: 16}

    # Convertir a decimal
    num = int(valor, bases[origen])

    # Convertir de decimal a la base destí
    if desti == 1:
        print("Resultat en binari:", bin(num)[2:])
    elif desti == 2:
        print("Resultat en octal:", oct(num)[2:])
    elif desti == 3:
        print("Resultat en decimal:", num)
    elif desti == 4:
        print("Resultat en hexadecimal:", hex(num)[2:].upper())


# ------------------------------
#        PROGRAMA PRINCIPAL
# ------------------------------

op = 1
while op != 0:
    op = menu_principal()

    if op == 1:
        print("Estic passant per la calculadora decimal\n")
        calculadora_decimal(menu_calculadora())

    elif op == 2:
        print("Estic passant per la calculadora real\n")
        calculadora_real(menu_calculadora())

    elif op == 4:
        canvi_base()

    else:
        print("Gràcies per utilitzar la meva calculadora!\n")
        op = 0
