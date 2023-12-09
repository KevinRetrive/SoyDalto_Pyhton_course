# Una clase abstracta, es una receta como toda clase,
# PERO que no podemos instanciar (crear objetos), es como una plantilla para crear clases a partir de ella

# Implementar un método significa definir como va a funcionar

from abc import ABC, abstractclassmethod # Le indicamos que estamos usando un método abstracto
# abc es un módulo de PY, ABC es una clase y abstractclassmethod es un decorador
# abc es una clase auxiliar, sólo que tiene una meta clase de ABC (creo que una meta clase, es la clase de una clase)
# Un método abstracto, es un método declarado pero sin ninguna implementación, por ej:
# creo el método hacer sonido, pero no le hago código, ya que esto será una plantilla tq cuando cree una clase a partir de esta, ahí si lo implemente

class Persona(ABC): # Con esto ya hicimos una clase abstracta
    @abstractclassmethod # Y con este decorador ya le decimos que vamos a crear un método abstracto
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass  # Porque las personas no tienen todas = actividades
    
    def presentarse(self): # Y creamos esta como plantilla de presentación general, para tod@s
        print(f"Hola, me llamo: {self.nombre} y tengo: {self.edad} años")

#alguien = Persona("Flor",22,"Femenino","Estudiante")
# Me tira error porque me dice q es una clase abs con método abs
# Si le quitara el ABC dentro de persona, dejaría de ser abstracta la clase y si fucnionaría
# Si sólo quitara el @abstractclassmethod no sería suficiente, xq la clase seguiría abs
# Ya tenemos lista nuestra plantilla que nos permite crear personas:

# Ahora vamos a crear dos clases más

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    # Ahora si implemento el método, y cuando lo realice no me tirará error
    def hacer_actividad(self):
        print(f"Mi actividad principal es: {self.actividad}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Mi profesion es: {self.actividad}")



Flor = Estudiante("Flor",22,"Femenino","Ir al gym")
Kev = Trabajador("Kev",26,"Masculino","Ingeniero")

Flor.presentarse()
Flor.hacer_actividad()
Kev.presentarse()
Kev.hacer_actividad()
# Para eso sirven las clases abs, poder implementar una plantilla para no tener que crear la clase de 0,
# cuando tenemos sub clases con atributos similares, pero en otros aspectos requieren métodos o atributos diferentes
# pero... ¿ por qué hacer este lio que es muy similar a la herencia múltiple?
# Es cierto que podes llegar al mismo resultado, pero trae otros beneficios hacerlo de manera abstracta
# como obligar a heredar determiandos métodos, fomentar el polimorfismo (todas las sub clases de personas harán actividad)
# mayor seguridad, claridad, plantilla, etc.
