# a = [1, "a", "capça"[2], 1, "a"]
a = [10, 9, 8, 7, 6, 5, 1, 2, 3 ,4]
# Pasar els elements de la llista a string
for i in range(len(a)):
    a[i]=str([i])
# Crear un unic string separat per guio
print("-",join(a))




"""
print(a[::-1]) # Retorna una llista invertida, però no modifica l'original
print(a)
print(a.reverse()) # No retorna res, però modifica la llista original
print(a)

a.sort()
print(a)
for i in range(len(a)):
    a[i]=str(a(i))
a.sort()     
print(e)

c= "capça" in a
print(c)
c = a.pop(2)
print(c)
a[0]= "Hola, som en Ramis"
del a [:]
a.append(10)
a.append("cadena nova")
a.append([10,11,12])
a.extend((10,"cadena nova",[10,11,12]))
print(a)
"""