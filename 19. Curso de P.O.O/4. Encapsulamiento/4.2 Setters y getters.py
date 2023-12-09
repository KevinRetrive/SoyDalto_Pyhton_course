class persona:
    def __init__(self, nombre, edad, nacionalidad):
     self.__nom = nombre  
     self.__age = edad
     self.__nac = nacionalidad
     
    def get_nombre(self):
         return self.__nom
     
    def set_nombre(self, new_name):
        self.__nom = new_name

dalto = persona("Lucas", 26,"Argentino")
# print(dalto.__edad) # Accedemos pero no es la forma correcta
# Debemos crear/usar un set/getter
# Lo mismo si estuviera como MP

nombre = dalto.get_nombre()
print(nombre)

dalto.set_nombre("Pepito")
nombre = dalto.get_nombre() # Y vuelvo a usar get para obtener/acceder el valor con el nuevo nombre
print(nombre)

