def mostrar_majors_que(tupla, valor):
    for numero in tupla:
        if numero > valor:
            print(numero)
quantitat = int(input("Quants valors vols introduir? "))

llista_valors = []

for i in range(quantitat):
    num = int(input("Introdueix un valor enter: "))
    llista_valors.append(num)
    
tupla_valors = tuple(llista_valors)

print("\nValors majors de 18:")
mostrar_majors_que(tupla_valors, 18)
