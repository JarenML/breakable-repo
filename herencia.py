class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print("El animal esta comiendo")

class Ave(Animal):
    pass


class AveVoladora(Ave):
    def volar(self):
        print("El ave esta volando")


ave_voladora = AveVoladora('aguila', 6)


class AveNoVoladora(Ave):
    pass
    

class Perro(Animal):
    def ladrar(self):
        print("el perro esta ladrando")

