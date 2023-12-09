# Crear una clase "estudiante" con atributos "nombre, edad, grado"
# Además crear un método "estudiar()" que no devuelva "f"El estudiantes {} está estudiando""
# Crear un instancia y usar el método, pero se pide generar una interacción con el usuario
# Se requiere que el usuario se ingrese como estudiante (nombre, edad, grado) y que ponga estudiar fjksnjs

class estudiante:
    def __init__(self, nombre, edad, grado):
     self.name = nombre  
     self.age = edad
     self.level = grado + " Grado"
     
    def estudiar(self):
        print(f"""\n El estudiante {self.name}:
              - Tiene {edad} años de edad,
              - Y se encuentra en {grado} Grado
              """)

print("Para inscribirse rellene sus datos")
nombre = input("Nombre y apellido: ")
edad = input("Edad: ")
grado = input("Grado: ")

alumne1 = estudiante(nombre,edad,grado)
# Soy crack lo hice sólo sin mirar de esta manera, ahora chequeo si hay una mejor...
#alumne1.estudiar() 
# Así lo hice yo pero para no logré que el usuario sea el que ingrese la función y que además,
# no importe si la escribe con minusc. o mayusc.
# Se hace así:

while True:
# Hago un bucle para que si escribo mal la función estudiar que cree para que me devuelva los datos está mal,
# poder pedirle que la vuelva a escribir, y que sea indistinto si escribe minusc. o mayusc.
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
     alumne1.estudiar() 
# El problema de esto es que no frena al escribirlo bien y no halle la forma de darle un stop cuando el usuario ingresa la palabra