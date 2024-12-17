class Animal:
    totalAnimales = 0
    mamiferos = 0
    aves = 0
    reptiles = 0
    peces = 0
    anfibios = 0

    def __init__(self, nombre, edad, habitat, genero, zona=None):
        Animal.totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self.zona = zona

    def movimiento(self):
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        return (f"Mamiferos : {Animal.mamiferos}\n"
                f"Aves : {Animal.aves}\n"
                f"Reptiles : {Animal.reptiles}\n"
                f"Peces : {Animal.peces}\n"
                f"Anfibios : {Animal.anfibios}")

    def toString(self):
        base = (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} "
                f"y mi genero es {self._genero}")
        if self.zona and self.zona.zoo:
            return f"{base}, la zona en la que me ubico es {self.zona.getNombre()}, en el {self.zona.getZoo().getNombre()}."
        return base

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero