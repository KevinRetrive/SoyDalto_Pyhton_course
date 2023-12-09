# Métodos especiales, como __init__ son métodos ya creados por PY, no se pueden re definir o re crear
# Son funciones creadas con dos guiones bajos al inico y al final
# Tal como __init__ vimos que es un constructor, construye los objetos de una clase, y le cargamos los atributos que va a tener ese objeto
# Veremos otros:

# __str__ devuelve una representación del objeto en una cadena de texto
# es decir, sólo llamando al objeto, ya me devuelve en pantalla lo que le diga que me muestre

# __repr__ es similira al anterior, pero sirve para representar y "construir" el objeto

# __add__(self,otro) otro hace referencia a lo que queremos sumar, ver ejemplo

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Persona (nombre = {self.nombre}, edad = {self.edad})"

    def __repr__(self):
        return f'Persona ("{self.nombre}",{self.edad})'

    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)
# Con este código, acabamos de definir como se van a comportar los objetos de esta clase al sumarlos!!!
# Si esto no existiera, me tiraría error, sería imposible sumar dos objetos sin definir cómo
# Esto se llama sobrecarga de operadores, y existen muchos más (le saque foto)

alguien = Persona("Flor_",22)
yo = Persona("Kev_",26)
mini_flor = Persona("y_mini_flor",12)
pareja = alguien+yo+mini_flor

repre = repr(alguien) # Obtengo una representación del objeto para reconstruirlo
resultado = eval(repre) # Reconstruyo el objeto y lo obtengo

print(alguien) # Vemos que solo ingreso el objeto "alguien" y ya me devuelve el código}
print(resultado) # Con el .edad o .nombre me muestra sólo esos valores, sino así la representación
print(pareja)
