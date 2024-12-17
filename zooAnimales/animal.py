class Animal:
    totalAnimales = 0
    mamiferos = 0
    aves = 0
    reptiles = 0
    peces = 0
    anfibios = 0

    def __init__(self, nombre, edad, habitat, genero, zona=None):
        Animal.totalAnimales += 1
        self.__nombre = nombre
        self.__edad = edad
        self.__habitat = habitat
        self.__genero = genero
        self.zona = zona

    def movimiento(self):
        return "desplazarse"

    def totalPorTipo():
        return (f"Mamiferos: {Animal.mamiferos}\nAves: {Animal.aves}\n"
                f"Reptiles: {Animal.reptiles}\nPeces: {Animal.peces}\nAnfibios: {Animal.anfibios}")

    def toString(self):
        base = (f"Mi nombre es {self.__nombre}, tengo una edad de {self.__edad}, habito en {self.__habitat} "
                f"y mi genero es {self.__genero}")
        if self.zona and self.zona.zoo:
            return f"{base}, la zona en la que me ubico es {self.zona.getNombre()}, en el {self.zona.getZoo().getNombre()}."
        return base

    def getNombre(self):
        return self.__nombre
