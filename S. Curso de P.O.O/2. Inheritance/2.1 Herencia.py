# La herencia es uno de los pilares fundamentales de la POO
# Lo que hace es permitir a la clase hija acceder a todos los métodos y tener las propiedades de la clase padre
# Es decir, que podamos tener una clase dentro de otra, por ejemplo que la clase estudiante este en una clase "persona"
# Y que cumpla los atributos de persona pero con otros atributos nuevos para ser estudiante

class persona:
    def __init__(self, nombre, edad, nacionalidad):
     self.nom = nombre  
     self.age = edad
     self.nac = nacionalidad
     
    def hablar(self):
        print("Hola, estoy hablando un poco")

class empleado(persona):  # Lo único NUEVO es agregar dentro del parentesis la clase padre!!! tucs
    #pass # Con esta función podemos decirle que dejamos la clase vacía sin cargarle nada y no nos tirará error,
 # sirve también para cuando queremos crear una función con def por ejemplo 
  
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        # Debemos colocar los atributos heredados y los nuevos
     super().__init__(nombre, edad, nacionalidad) # Debemos colocar los atributos que quiero que herede
     # Con super() "metemos" un constructor adentro de otro para que funcione lo de heredar
     self.tra = trabajo
     self.sal = salario
     
     # Incluso podría reescribir el método de la clase padre, por ej:
    def hablar(self):
        print("Ahora estoy en la clase hija")
    
Roberto = empleado("Roberto",34,"Argentino","Obrero",120.000) # Ahora debo agragar los atributos de la clase hija
print(Roberto.age)
Roberto.hablar()
# Podemos ver como usamos la clase empleado, a la cual no le cargamos nada,
# pero nos devuelve el dato de lo heredado en la clase persona
# y si en la línea 19 hubiera usado la clase persona, funcionaría exactamente igual

# También se pueden escuchar las denominaciones superc clase (clase padre) y sub clase (clase hija)
# Hasta acá, esto se denomina herencia simple

# Luego esta el concepto de la clase jrarquica, (en código es lo mismo),
# pero en conceptos es cuando todas las clases son hijas de una padre
# Ej. Persona es el padre de empleados, estudiantes, jubilados, etc, son todos subclases de personas

# Y por último tenemos la herencia múltiple, es decir que una clase herede de dos o más, ej en el siguiente archivo
