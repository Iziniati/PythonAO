import os

directori = "/home/izan/Ao/PythonAO"
os.makedirs(directori, exist_ok=True)
os.chdir(directori)
companys = ["Izan", "Pau", "Lucas", "Eneko", "Rafa"]
with open("Ex12.txt", "w", encoding="utf-8") as fitxer:
    for nom in companys:
        fitxer.write(nom + "\n")
professors = ["Joan", "Marta"]
with open("Ex12.txt", "a", encoding="utf-8") as fitxer:
    for nom in professors:
        fitxer.write(nom + "\n")
llista_noms = []
with open("Ex12.txt", "r", encoding="utf-8") as fitxer:
    for linia in fitxer:
        llista_noms.append(linia.strip())
print(llista_noms)
