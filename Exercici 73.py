from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        print(f"Sóc un {self.especie} i tinc {self.edat} anys.")

class Cavall(Animal):
    def xerrar(self):
        print("Neigh!")

    def mourem(self):
        print("El cavall galopa.")

class Dofi(Animal):
    def xerrar(self):
        print("Click-click!")

    def mourem(self):
        print("El dofí neda ràpidament.")

class Abella(Animal):
    def xerrar(self):
        print("Bzzzz!")

    def mourem(self):
        print("L'abella vola.")

    def picar(self):
        print("L'abella pica!")

class Humà(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom = nom

    def xerrar(self):
        print("Hola!")

    def mourem(self):
        print(f"{self.nom} camina.")

class Fiet(Humà):
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares = pares

    def nompares(self):
        print(f"Els pares de {self.nom} són: {', '.join(self.pares)}")

class Centaure(Cavall, Humà):
    def __init__(self, especie, edat, nom):
        Cavall.__init__(self, especie, edat)
        self.nom = nom

    def xerrar(self):
        print("Som un centaure!")

    def mourem(self):
        print(f"{self.nom} corre com un cavall i camina com un humà.")

class Xou:
    def xerrar(self):
        print("Xou fa soroll!")

    def mourem(self):
        print("Xou es mou!")

    def quisoc(self):
        print("Sóc un objecte Xou.")

elements = [
    Cavall("Cavall", 5),
    Dofi("Dofí", 3),
    Abella("Abella", 1),
    Humà("Humà", 30, "Joan"),
    Fiet("Humà", 10, "Fiet", ["Anna", "Pau"]),
    Centaure("Centaure", 7, "Cen"),
    Xou()
]

for elem in elements:
    print(f"\n{type(elem).__name__}:")
    elem.quisoc()
    elem.xerrar()
    elem.mourem()
    if isinstance(elem, Abella):
        elem.picar()
    if isinstance(elem, Fiet):
        elem.nompares()
