# Creando un conjunto con set
conjunto = set(["dato1", "dato2"])

# No podría poner en dato1 o dato2 un dato modificable como una lista, por ej:
# conjunto2 = set(["dato1", [ "dato1lista" , "dato2lista" ]])
# No puedo insertar una lista porque es modificable, sin embargo una tupla, sí podría
# No puedo poner un conjunto dentro de otro, a menos que use la función frozenset

# print(conjunto2) # Me tira error

# Función frozenset

conjunto1 = frozenset(["dato1", "dato2"]) # Creamos un conjunto inmutables pero se puede llamar en otro conjunto
conjunto2 = {conjunto1 , "dato3" }
print(conjunto2)

# Un sub-conjunto, son algunos datos pertenecientes a un dado conjunto
# Es decir este conjunto que contiene los mismo datos del sub-conjunto, posee más datos además de esos
# y se denomina superconjunto, ejemplo:

conjuntoA = { 1 , 3 , 5, 7 }
conjuntoB = {1, 3, 7 }
# ¿Cómo verificamos si un conjunto es subconjunto de otro
# Usamos el método .issubset() que devuelve True or False

resultado = conjuntoB.issubset(conjuntoA)
print(resultado) # True

# Otra forma es usando el <=, es exactamente igual que el método
# Los ponemos al revés para probar que debería ser False
resultado2= conjuntoA <= conjuntoB
print(resultado2) # False

# ¿Cómo verificamos si un conjunto es superconjunto de otro
# Usamos el método .issuperset(), de la misma manera
# O sino, también con >

# También podmeos verificar si hay al menos un n° en común
# Usamos el método .isdisjoint(), y devuelve True or False
# Si hay al mneos 1 elemento igual entre esos conjuntos devuelve False