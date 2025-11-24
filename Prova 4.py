a = [1,3,5,7, "a", "Capça", [2,3,4]]
for e in a:
    print(e)
for i in range(len(a)):
    a[i]*=2 # --> a[i]= a[i]*2
    print("la posició {} té el valor {}". format(i,a[i]))
for i,e in enumerate(a):
    print("La posicio {} té el valor {}".format(i,e))