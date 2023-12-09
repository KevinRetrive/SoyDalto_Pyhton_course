# Crear un sistemas para una escuela, con dos clases principales: Persona y Estudiante
# Persona, posee 2 atributos: nombre y edad, junto a un método que imprima estos
# Estudiante hereda de la clase persona y además tendrá un atributo y método para imprimir su grado
# Para heredar no olvides usar super() en __init__(). Finalmente crea una instancia para estudiante

class Persona:
    def __init__(self, nombre, edad):
        self.name = nombre
        self.age = edad
        
    def presentar_persona(self):
        return f"El nombre es: {self.name}\nY su edad: {self.age}"
        
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad) # SI usamos super NO poenmos self, si usamos la clase sí !!!
        self.grade = grado
    
    def estudiante_grado(self):
        print(f"El nombre es: {self.name}\nY su edad: {self.age}\nY su grado es: {self.grade}")
    

Flor = Estudiante("Florencia Hueche", 22, "universitario")
Flor.estudiante_grado()
