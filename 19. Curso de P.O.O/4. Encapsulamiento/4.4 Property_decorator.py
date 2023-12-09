# Las propiedades son getters y setters
# Aprendimos el concepto de decoradores para poder simplificar el concepto que sigue
# El decorador property, en el uso de setters y getters

class persona:
    def __init__(self, nombre, edad, nacionalidad):
     self.__nom = nombre  
     self.__age = edad
     self.__nac = nacionalidad
     
     # Este decorador, es especial, es reservado para las clases, para indicarles que el siguiente método es un getter, incluso para notaciones MP
     # Le dice, che no vas a ser una función, vas a ser una propiedad...
    @property
    def get_nombre(self):
         return self.__nom

    @get_nombre.setter # Le indicamos que serán ambos métodos iguales (ambos propiedades decoradoras)
    def set_nombre(self, new_name):
        self.__nom = new_name

    @get_nombre.deleter
    def deleter_nombre(self):
        del self.__nom # del es un operador que nos elimina valores, le indicamos cual queremos eliminar

# No sería una sobre carga de métodos, sino 2 decoradoras diferentes (propiedades distintas, uno para acceder y otra para modificar)

Kev = persona("Kevin",26,"Arg")
# Y ahora puedo llamar a la función de esta manera:
nombre = Kev.get_nombre # Y no preciso poner los () al final de la propiedad
print(nombre)

# Recordar que como es un getter y no un setter, no permite modificarlo re nombrando así:
# Kev.get_nombre = "Roberto" no me lo cambiaría
# Kev.__nom = "Roberto" y usando la original tampoco me dejaría

# Pero si lo hago con el setter...
Kev.set_nombre = "Roberto"
nombre = Kev.set_nombre
print(nombre)

# Y ahora quiero eliminar a Roberto:
del Kev.deleter_nombre
# Es necesario el código de arriba dentro de la clase, sino esto no funcionaria wey
print(nombre) # Debería tirar error, porque elimino ya a Roberto, pero NO FUNCIONA

# Todo esto ¿para qué? Porque no queremos que se acceda a la propiedad __nombre
# De esta forma le permitimos acceder o modificar el valor igualmente

# Esta es la forma más óptima de realizar estos códigos
