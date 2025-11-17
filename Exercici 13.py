def menu_principal():
    opcio=0
    while opcio<1 or opcio>3:
        opcio = int(input(""" Eligeix una opció:
                      1. calculadora decimal
                      2. calculadora real(floats)
                      3. sortir \n"""))
    if opcio>0 and opcio<4:
            return opcio
    else:
            print("L'opció seleccionada no és correcte, torni-ho a provar!!\n")

def menu_calculadora():
    opcio=0
    while opcio<1 or opcio>5:
        opcio=int(input("""eligeix una opció:
                    1. Suma
                    2. Resta  
                    3. Multiplicació
                    4. Divisió
                    5. Sortir
                    """))
    if opcio>0 and opcio<6:
         return opcio
    else:
        print("L'opció sececionada no es correcte, torna-ho a provar!!\n")

def calculadora_decimal(opcio):
    if opcio>0 and opcio<5:
        a = int(input("introdueix el primer nombre: "))
        b = int(input("introdueix el segon nombre: "))
    match(opcio):
        case 1:
            #suma
            print("Estic fent la suma! \n")
            c = a + b
            print("El resultat de suma {} + {} és {}".format(a, b, c))
        case 2:
            #resta
            print("Estic fent la resta! \n")
            c = a - b
            print("El resultat de resta {} - {} és {}".format(a, b, c))
        case 3:
            #multiplicació
            print("Estic fent la multiplicació! \n")
            c = a * b
            print("El resultat de resta {} * {} és {}".format(a, b, c))
        case 4:
            #divisió
            print("Estic fent la divisió! \n")
            c = a // b
            print("El resultat de resta {} / {} és {}".format(a, b, c))
        case _:
            print("Opció no valida, torna-ho a provar! \n")

def calculadora_real(opcio):
    if opcio>0 and opcio<5:
        a = int(input("introdueix el primer nombre: "))
        b = int(input("introdueix el segon nombre: "))
    match(opcio):
        case 1:
            #suma
            print("Estic fent la suma! \n")
            c = a + b
            print("El resultat de suma {} + {} és {}".format(a, b, c))
        case 2:
            #resta
            print("Estic fent la resta! \n")
            c = a - b
            print("El resultat de resta {} - {} és {}".format(a, b, c))
        case 3:
            #multiplicació
            print("Estic fent la multiplicació! \n")
            c = a * b
            print("El resultat de resta {} * {} és {}".format(a, b, c))
        case 4:
            #divisió
            print("Estic fent la divisió! \n")
            c = a / b
            print("El resultat de resta {} / {} és {}".format(a, b, c))
        case _:
            print("Opció no valida, torna-ho a provar! \n")

# programa Principal

op = 1
while op!=0:
   op = menu_principal()
   if op==1:
       #calculadora decimal
       print("Estic passant per la calculadora decimal")
       calculadora_decimal(menu_calculadora())
   elif op==2:
       #calculadora real
       print("Estic passant per la calculadora real \n")
       calculadora_real(menu_calculadora())
   else:
       print("Gràcies per emprar la meva calculadora \n")
       op=0
