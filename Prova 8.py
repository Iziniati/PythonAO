def factorial(n):
    if n>0:
        return n*factorial(n-1)
    else:
        return 1
#Programa principal
a = int(input("introdueix un nombre per fer el factorial"))



"""
def sumaun(l):
    for i,e in enumerate(l):
        l[i]=e + 1
    
# Programa principal
l=[5, 6, 7, 10]
print(l)
sumaun(l)
print(l)
sumaun(l)
print(l)


def ordenar(x, y):
    if x>y:
        return x,y
    elif y>x:
        return y,x
    else:
        return x,y
    
# Programa principal
v1 = int(input("Intro el 1r numero: "))
v2 = int(input("Intro el 2r numero: "))
v1, v2 = ordenar(v1, v2)
for e in range(v2, v1+1):
    print(e)

v1 = int(input("intro el 1r numero: "))
v2 = int(input("intro el 2n numero: "))
r = (v1*v2) //2 
for i in range(r, -1, -1):
    print(i)
"""