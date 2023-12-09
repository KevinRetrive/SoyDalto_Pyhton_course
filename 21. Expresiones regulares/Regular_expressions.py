# Importamos el módulo más común que se utiliza para trabajar con ER
import re # Ya incluido en la biblioteca de PY

# Tenemos distintas fucniones
texto = """Hola maestro, esta es la cadena 1. Como estas mi capitan?
Esta es la 2da línea.
Y esta es la 3era final crack.
"""
# Busqueda simple:
# Con la funcion search() o findall() podemos buscar coincidencia y las devuelve
resultado = re.search("Hola",texto)
resultado2 = re.findall("esta",texto,flags=re.IGNORECASE)
# Con search() me busca el 1er hola y 
# con findall() todos los hola, y le añadimos un 3er argumento para que no distinga entre mayúsculas y minúsculas
print(resultado)
print(resultado2)

# Expresiones regulares:

# Para poder aplicarlas debo usar la r dentro de los parentesis, indicando que ingresaré
# Una ER al igual que cuando uso la f para indicarle que entre {} ingreso una variable entre el texto.

# 1) \d -> busca digitos númericos del 0 al 9
print("-------------------------------------------------")
resultado3 =re.findall(r"\d",texto)
print(resultado3)
# Entonces con esto le decimos voy a buscar digitos numéricos del 0 al 9 en texto

# 2) \D -> busca TODO los caracteres MENOS digitos númericos
print("-------------------------------------------------")
resultado4 =re.findall(r"\D",texto)
print(resultado4)

# 3) \w -> busca caracteres alfa-númericos (a-z, A-Z, 0 a 9, y "_")
print("-------------------------------------------------")
resultado5 =re.findall(r"\w",texto)
print(resultado5)
# En PY el "_" se considera un caracter alfa-num, no así en otros lenguajes

# 4) \W -> busca TODO MENOS caracteres alfa-númericos (espacios, espacio de línea, comas, signos, etc)
print("-------------------------------------------------")
resultado6 =re.findall(r"\W",texto)
print(resultado6)

# 5) \s -> busca espacios en blanco

# 6) \S -> busca TODO MENOS espacios en blanco (comunes, tabs, espacios de linea [\n])

# 7) . -> busca TODO MENOS los espacios o "saltos" de linea [\n])
print("-------------------------------------------------")
resultado9 =re.findall(r".",texto)
print(resultado9)

# 8) \n -> busca los espacios o "saltos" de linea [\n])

# 9) \ -> cancela caracteres especiales (todo lo q no sea n° o letra o el "_")
print("-------------------------------------------------")
# Cancelando la función del punto y buscando puntos en texto
resultado11 =re.findall(r"\.",texto)
print(resultado11)

# podemos combinar esta busqueda por ej:
# usando una cadena que busque un n° aeguido de un punto y un espacio
print("-------------------------------------------------")
resultado12 =re.findall(r"\d\.\s",texto)
print(resultado12)

# 10) ^ (acento circunflejo) -> busca el comienzo de una línea
print("-------------------------------------------------")
# Acoplado a una serie de caracteres, me dira si esa serie esta al principio de la línea, ej:
resultado13 =re.findall(r"^Esta",texto,flags=re.M) 
# Si no estuviera al principio me devuelve lista vacía 
# con el 3er argumento lo convertimos en multi-linea, revisa el inicio de c/u
print(resultado13)

# 11) $ -> busca el final de una línea (al revés que el ^)
# Pero a diferencia del ^, se escribe al final de la palabra 
# o caracteres que quiero buscar al final de la linea
#resultado =re.findall(r"capitan$",texto,flags=re.M) 

# Despuéss tenemos los que son los grupos

# 12) {n} -> busca n=n° cantidad de veces el valor de la izquierda
print("-------------------------------------------------")
resultado14 =re.findall(r"\d{3}\s",texto)
# Le estoy indicando que busque los digitos como vimos y luego
# le digo que me traiga 3 veces lo que esta a la izquierda, o sea
# 3 digitos continuos y finalmente un espacio o sino devuelve lista vacía
print(resultado14)

# 13) {n,m} -> busca al menos n=n° cantidad de veces 
# y como máx m=n° cantidad de veces el valor de la izquierda
resultado15 =re.findall(r"\d{1,3}\s",texto)
print(resultado15)

# Ojo porque los {n,m} sólo toman lo 1ero que le indico a la izquiera pero si
# buscara "ab{1,2}" sólo aplicaria para la busqueda de la letra b. Para incluir
# a la letra a o al resto de caracteres o condiciones que esten a la izquiera debo hacer 
# lo siguiente que es armar conjuntos, es decir ponerlos entre parentesis:
#resultado15 =re.findall(r"(ab){1,3}\s",texto)
# O también si armamos un conjunto usando corchetes tiene otra función pero no entendí un pingo
# Creo que busca lo que le indico pero solo devuelve 1 vez lo que esta adentro del corchete

# 14) | -> busca lo que esta a la izquierda o a la derecha
print("-------------------------------------------------")
resultadofinal =re.findall(r"Esta|Hola",texto)
# Si encuentra ambas, devuelve ambas, sino sólo una
print(resultadofinal)


