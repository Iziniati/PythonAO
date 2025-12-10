import random


def generar_codi():
    codi = []
    for _ in range(4):
        codi.append(str(random.randint(0, 9)))
    return codi

def comprovar_jugada(codi_secret, codi_usuari):
    encert_correcte = 0
    coincidencies = 0


    codi_s = codi_secret.copy()
    codi_u = codi_usuari.copy()
    for i in range(4):
        if codi_u[i] == codi_s[i]:
            encert_correcte += 1
            codi_s[i] = codi_u[i] = None 
    for i in range(4):
        if codi_u[i] is not None and codi_u[i] in codi_s:
            coincidencies += 1
            codi_s[codi_s.index(codi_u[i])] = None

    return encert_correcte, coincidencies

# Programa principal
def jugar_mastermind():
    print("Benvingut al MasterMind simplificat!")
    codi_secret = generar_codi()
    intents = 0

    while True:
        codi_usuari = input("Introdueix un codi de 4 xifres: ")

        if len(codi_usuari) != 4 or not codi_usuari.isdigit():
            print("Has d'introduir exactament 4 números.")
            continue

        codi_usuari = list(codi_usuari)
        intents += 1

        encert, coincidencia = comprovar_jugada(codi_secret, codi_usuari)

        if encert == 4:
            print(f"Felicitats! Has endevinat el codi en {intents} intents.")
            break
        else:
            print(f"Xifres en la posició correcta: {encert}, coincidències: {coincidencia}")

# Executem el joc
jugar_mastermind()
