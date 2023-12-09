# Significa manejar la complejidad ocultando todos los detalles innecesarios, mostrando sólo las funciones relevantes
# No necesitamos saber cómo funciona internamente o cómo se desarrolló, sino cómo usarlo

class Auto():
    def __init__(self):
        self._estado = "apagado"
        
    def encender(self):
        self._estado = "encendiendo"
        print("El auto está encendido")
    
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
        
mi_auto = Auto()
mi_auto.conducir()
# Acá ya se explica el concepto de abstracción, porque el usuario sólo ejecuta el método y reciba una respuesta
# Pero jamás se entera que el código revisa si el auto esta encendido o apagado, o cómo lo hace

# Hay otros tipos de abstracción más específico, como en clases por ej. La que vimos recién es como la general
# Vamos a ver cómo crear clases y métodos abstractas
