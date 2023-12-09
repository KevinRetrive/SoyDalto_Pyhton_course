# A diferencia de los módulos, los paquetes son muchos módulos, es decir, muchos archivos .py
# Creamos dos copias del archivo saludar, Hola_normal y Hola_raro
# Supongamos que quiero importar un paquete (una carpeta con muchos módulos dentro), entonces metemos
# las copias de estos archivos en una carpeta para poder practicar esto

# IMPORTANTE
# Pyhton reconoce las carpetas como paquetes si en ellas creamos un archivo "file" que se llame: __init__.py
# Para que veamos que lo reconoció:

import Paquete
print(type(Paquete)) # Nos dice que es un módulo... porque un paquete no deja de ser un módulo con módulos je
# Si le borrara el archivo __init__.py no diría igual que es un módulo pero la diferencia está en el enrutamiento al módulo/paquete
# Y nos daría error al hacer esto:  print(type(Paquete.__path__)) al buscar los archivos en el subdirectorio
# Al agregar este archivo __init__ entiene que es un paquete y lo agrega y muestra la ruta en la lista

# Entonces si quiero acceder al paquete
import Paquete.Hola_normal as Phn
print(Phn.saludar("Ana"))

# Después están los sub-paquetes, que en si es tener a un paquete dentro de otro, pero no es complicado, es similar el procedimiento
# Ej: import Paquete.Subpaquete.Modulo y dentro del subpaquete deberia crear el archivo __init__.py !!!
# ¿Que pasa si tengo dos archivos llamados iguales (una carpeta y un archivo)..? siempre tiene prioridad la carpeta, se invocará esta
