def comptar_vocals(paraula):

    paraula = paraula.lower()

    a = paraula.count("a")
    e = paraula.count("e")
    i = paraula.count("i")
    o = paraula.count("o")
    u = paraula.count("u")
    print("Hi ha", a, "a's,", e, "e's,", i, "i's,", o, "o's i", u, "u's.")


# Programa principal
comptar_vocals("Ratapinyada")  

