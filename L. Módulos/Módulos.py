# ¿Qué es un módulo?
# Cualquier archivo .py
# Desde un módulo puedo llamar a otro y usar todo lo que hice en dicho módulo
# Existen tres tipos:
# - Módulos de Py (creados por Python con lenguaje C)
# - Módulos de terceros (creados por personas, librerias)
# - Módulos propios

# A modo de ejemplo llamaremos al módulo saludar.py de esta carpeta:
# Debemos usar la función import para importar el módulo

#import Say_hello # Se denomina name-space el typo de código del módulo, así como hay strings, o listas, etc.
# El módulo aparte se comporta como un objeto!
# IMPORTANTE
# Por lo cual todas las funciones de ese módulo pasan a ser un método!!!!

#saludo = Say_hello.saludar("Kevin")
#print(saludo)

# Podemos utilizar la función "as" que actúa como el =, pero no es lo mismo
# Con ella podríamos modificar la forma de llamar al módulo en este script, por ejemplo:

#import Say_hello as Hi # Le ponemos el nombre que queremos (+ corto y simple)
#saludo = Hi.saludar("Kevin")
#print(saludo)

# Pero como se observa, la función import no trae TODO lo que esta en el módulo y lo ejecuta
# ¿Pero si tenemos un módulo enorme con muchas funciones y sólo queremos usar una especifica?
# Utilizamos la función "from" de la siguiente manera:

#from Say_hello import saludar as S,saludar_raro as SR
# Así podemos importar LO QUE SEA que hayamos definidos en el módulo, clase, objeto, método, función
# Agregamos otro saludo para que veamos que se pueden importar más de uno a la vez
# importamos 2 funciones y les cambiamos el nombre
#saludo = S("Kevin")
#saludo_r = SR("Fran")

#print(saludo)
#print(saludo_r)
#print(dir(Hi)) # Recuerden que dir me tira todas las propiedades y métodos que se pueden usar para este tipo de código, incluso las que definimos nosotros
#print(Hi.__name__) # Este método nos muestra el nombre real del módulo que estamos importando
#print(__name__) # Así sólo accedemos al nombre de este modulo, los nombres reales no se pueden cambiar

# Luego de import en la linea 31 si colocamos un "*" en vez de todo lo especificado, le estamos diciendo que
# importe TODO, pero como vimos no es recomendable a pesar de ser una paja tener que andar especificando

# OBS en el caso que el archivo que queremos importar esté en otra carpeta DENTRO se debe poner:
# "from NOMBRECARPETA.NOMBREMODULO" es decir precedido por el nombre de la carpeta y un punto y listo

# OBS en el caso que el archivo que queremos importar esté en otra carpeta AFUERA se debe poner:

import sys
print(sys.builtin_module_names) # built-in (construidos en el sistema, en Py con lenguaje C)
# Esto nos devuelve una tupla con todos los nombres de todos los módulos que estan en sys
# Si no sabemos donde están podemos usar lo siguiente
#print(sys.path) # Nos da las rutas a todos los módulos, el 1ero será en el que estamos ahora siempre

# ENTONCES, si sabemos que el módulo que queremos esta una carpeta para atrás o un acceso para atrás, 
# podemos copiarnos ese acceso y hacer lo siguiente para llamar a este módulo especifico (COPIAR Y PEGAR ESE ACCESO HASTA UNA CARPETA ANTES)
sys.path.append("c:\\Users\\Kevin\\OneDrive\\Escritorio\\Pyhton\\13. Enrutamiento de módulos")
print(sys.path)

# Copie y pegue el módulo Say_hello dentro de la carpeta 13 pero lo renombre como Hola, para probar:
import Hola # Aunque me marque el Hola como error NO es un error!!!
print(Hola.saludar_en("Michi"))




