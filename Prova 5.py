a = (1, 2, 4, 4, 2, 4, 2, 1, 2, 3, 1, 3, 1, 4, 2, 1, 3, 4 ,1, 2, 4, 3, 1) # llista
b = set(a) # onjunt/set
c = list() # Llista buida on gurardes elements i numero de repeticions
for e in b:
    c.append([e,a.count(e)])
print(c)

"""
b = a.index(4)
print()

b = a.count(1)
print(b)

x, y, z=a
print("x= {}, y= {}. z={}".format(x, y, z)) 
"""