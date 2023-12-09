# EJ. de herencia múltiple, calse persona y clase artista
# El artista tendrá una habilidad

class persona:
    def __init__(self, nombre, edad, nacionalidad):
     self.nom = nombre  
     self.age = edad
     self.nac = nacionalidad
     
    def hablar(self):
        print("Hola, estoy hablando un poco")


class artista:
    def __init__(self, habilidad):
     self.hab = habilidad
     
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.hab}"
    # Recordar que con return, no me escribe la respuesta sino que la guarda en su memoria, a diferencia del print


class EmpleadoArtista(persona,artista):
    # Sub clase que hereda, de otras dos clases y que a su vez posee nuevos atributos (salario, empresa)
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        persona.__init__(self, nombre, edad, nacionalidad)
        artista.__init__(self,habilidad)
    # En el caso de haber más de una clase padre, en vez de super() debo usar el nombre de la clase que corresponde
        self.sal = salario
        self.emp = empresa
     
    def mostrar_habilidad(self):
        return f"No hay habilidad"

    def presentarse(self):
        print(f" Usando self: {self.mostrar_habilidad()}\n Usando super(): {super().mostrar_habilidad()}")
    # Si usaba print me tiraba None al final, por eso uso return
    # Si en la línea 35 usará self.mostrar_habilidad() funcionaría igual pero podría generar un problema si editara la clase
    # PERO, en este caso debemos usar super porque es un método que esta heredado, es decir viene de arriba de alguna de las clase padre
    # O también si hubiera un método en esta clase con el mismo nombre, me traería esa, y no la de la clase heredada
    
Roberto = EmpleadoArtista("Roberto",43,"Argentino","Cantar",100000,"Aluar")
Roberto.presentarse()

# OBS: Usar siempre return, salvo en donde quiero que me escriba en el workflow la respuesta deseada

# OBS2: Si una de las clase padre fuera un módulo (es decir, está pero no podemos verlo), podría hacer lo siguiente
# Con la función issubclass() me responde si el primer argumento es subclase del 2do
Herencia = issubclass(EmpleadoArtista,artista)
print(Herencia) # Devuelve True

# OBS3: artista y persona no se relacionan de NINGUNA forma en este caso

# OBS4: Con la función isinstance() podemos ver si un objeto es una instancia de una clase. Ej:
instancia = isinstance(Roberto,EmpleadoArtista) # Los argumentos funcionan de igual forma pero,
# En este caso, cualquiera clase que le ingrese devolvería True, porque es un objeto que pertenece a todas las clases por la herencia múltiple
print(instancia) 

# OBS5: En el caso de tener dos atributos de clase con igual nombre, es decir, por ejemplo que en persona también hubiese un atributo llamado habilidad,
# O en el caso de que hubiera dos métodos con igual nombre, lo que define la prioridad es el MRO (Método de resolución de orden)
# El MRO de Python lo veremos en el siguiente archivo
