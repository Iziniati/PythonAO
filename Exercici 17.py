"Definir una funció que calculi la longitud de una llista o de una cadena donada. Prova-la amb diferents exemples."

def ex17(a):
    return len(a)

#programa principal
a= [1, 3, 4, "pere", [3,4],"a",[1, [3,4],5]]
print(ex17(a))
b = "Som en Joan Ramis, que tal estas?"
print(ex17(b))
c = []
print(ex17(c))