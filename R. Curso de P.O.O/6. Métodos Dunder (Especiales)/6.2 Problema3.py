# Crear un juego de fusión
# Crear personajes que se puedan fusionar
# y que formen un nuevo personaje q tenga más poder

# Se debe modificar el operador "+"
# Use la formula: el promedio del poder de ambos al cuadrado

class Personajes:
    def __init__(self, nombre, fuerza, velocidad):
        self.nom = nombre
        self.fuer = fuerza
        self.vel = velocidad
    
    def __repr__(self):
        return f"{self.nom} (Fuerza: {self.fuer}, Velocidad: {self.vel})"
        
    def __add__(self,otro_pj):
        nuevo_nombre = self.nom + "-" + otro_pj.nom
        nueva_velocidad = round(((self.vel + otro_pj.vel)/2)**2) # redondeamos con round()
        nueva_fuerza = round(((self.fuer + otro_pj.fuer)/2)**2)
        return Personajes(nuevo_nombre,nueva_fuerza,nueva_velocidad)


DGZ1 = Personajes("Goku",4,6)
DGZ2 = Personajes("Vegeta",2,4)
DGZ3 = Personajes("Krillin",1,1)
Gogeta = DGZ1+DGZ2
Raro = Gogeta+DGZ3
print(Gogeta)
print(Raro)
# Crear un juego, donde el usuario cree los personajes con sus valores de atributos y se fusionen nuevos.. ni gana


