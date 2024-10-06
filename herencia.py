class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print("El animal esta comiendo")

class Ave(Animal):
    pass


class AveVoladora(Ave):
    def __init__(self, nombre, edad, altura_vuelo):
        self.nombre = nombre
        self.edad = edad
        self.altura_vuelo = altura_vuelo

    def volar(self):
        print("El ave esta volando")


class Pinguino(AveNoVoladora):
    pass

ave_voladora = AveVoladora('aguila', 6, 200)


class AveNoVoladora(Ave):
    pass
    

class Perro(Animal):
    def ladrar(self):
        print("el perro esta ladrando")

