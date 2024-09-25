class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print("El animal esta comiendo")

animal = Animal("Rex", 5)

animal2 = Animal("Panda", 2)

animal3 = Animal("Michifus", 6)    


class Perro(Animal):
    def ladrar(self):
        print("el perro esta ladrando")

perro1 = Perro("Toby", 3)

perro2 = Perro("Firulais", 1)
