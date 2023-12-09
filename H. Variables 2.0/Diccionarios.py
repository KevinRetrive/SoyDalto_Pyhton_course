# Podemos crear diccionarios como ya sabemos con las {}
# O usar la funcion dict()
diccionario = dict( nombre = "kevin" , apellido = "retrive" )
# OBS para crear tuplas, listas, diccionarios... vacíos si o si es creandolos usando la función, no manualmente
# Recordar que a la variable que nombro, se llama clave, y el dato que le asigno, valor

# Podemos poner como claves tuplas(), pero no listas[] o conjuntos {} porque no son hasheables
# A menos que utilice la función frozenset()
diccionario={frozenset(["kevin","retrive"]): "Jajaj"}

# Otra forma de crear diccionarios es con el método .fromkeys()
# Permite crearlo con todos los valores nones (sin asignar)
# Se utiliza precedido de la función dict y el argumento como lista entre []
diccionario=dict.fromkeys(["nombre", "apellido", "suscriptores"])

# Si no uso corchetes, me crea para cada caracter un none, definiendolos como keys
diccionario=dict.fromkeys("nombre") # Para cada letra como key me da un none
# Porque el primer dato es un iterable, si le cargo un segundo argumento, a cada letra le asignará ese argumento en vez de none
diccionario=dict.fromkeys("nombre","apellido")

# También puedo combinar los casos, es decir usar corchetes para generar el diccionario con .fromkeys() y un último argumento fuera
# de los [] para que le asigne ese valor a todos, en vez de none. Ejemplo:
diccionario=dict.fromkeys(["nombre", "apellido", "suscriptores"], "No sé")

print(diccionario)

# También podemos hacer print de un elemento en específico, al igual que en las listas o las tuplas
print(diccionario["nombre"])
# Sin embargo ¿Cómo hacemos para traer un valor en los conjuntos?
# La unica forma es iterando, porque los conjuntos son iterables, que veremos en el siguiente tema
# Todas las variables que ocntengan más de un elemento son iterables
