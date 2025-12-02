for i in range(1,1001):
    if i%9==0 or i%7==0 and i%5!=0 and i%8!=0:
        print(i)
print("Has inserit un numero que no es valid, adéu!")

"""
((v1>=5 and v1<=10) or (v1>=15 and v1<=20) or (v1>=25 and v1<=30)) and v1!=6 and v1!=16 and v1!=26:

v1 = 2
while ((v1>=1 and v1<=1000) and (v1%2==0)):
    v1 = int(input("introdueix operador: "))
"""