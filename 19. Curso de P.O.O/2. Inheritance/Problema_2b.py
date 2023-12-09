# Estamos modelando animales en un ZOO
# Hay 3 clases: Animal, Mamiferos, Aves
# Animal debe tener un método llamado comer, mamifero -> amamantar y ave, volar
# Luego, hay una clase murcielago, ue hereda de mamifero y ave, en ese orden
# Por lo tanto debe ser capaz de amamantar, volar y comer, observar cómo cambia el MRO al usar super()

class Animal:
    def comer(self):
        print("Los animales comen")
    
class Mamiferos(Animal):
    def amamantar(self):
        print("Los mamiferos amamantan")

class Ave(Animal):
    def volar(self):
        print("Las aves vuelan")

class Murcielago(Mamiferos,Ave):
    pass

chupasangre = Murcielago()
chupasangre.comer()
chupasangre.volar()
chupasangre.amamantar()
print(Murcielago.mro())

colibri = Ave()
colibri.comer()
colibri.volar()
#colibri.amamantar() # Me tira error, me dice que colibri no es un objeto con atributo amamantar,
# y eso ocurre porque no pertenece a la clase mamiferos

