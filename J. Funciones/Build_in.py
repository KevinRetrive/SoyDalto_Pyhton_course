# Las funciones son simplificaciones de códigos, es defir realizan una acción a partir de un código, nos ahorran pasos
# Podríamos, a veces, llegar al mismo resultado escribiendo un código paso a paso, pero por suerte, hay personas que se encargaron
# de crear funciones ;)))
# Las build in son funciones creadas por Pyhton y veremos algunas, además de las que ya vimos
# Hatsa ahora conocemos print(), input(), type(), max(), min()

# Función round()
# redondea al entero más cercano, o al decimal indicado según el 2do argumento
num = round(12.846573,2)
print(num)
# TAREA optimizar los ejercicios prácticos, redondeando con la función y no haciendo cuentas como hicimos

print("-----------------------------------")
# Función bool()
# False --> 0, vacío, False o ninguno
# True --> Distinto de 0 o cadena de texto no vacía
F = bool(None)
print(F) # Como pusimos argumento vacío o None devuelve Falso
# Si le pasamos una lista vacía, devuelve Falso, idem para tupla, conjunto, diccionario
print("-----------------------------------")
T = bool(-5)
print(T)
print("-----------------------------------")

# Función all(), similar a bool() pero comprueba todos los elementos a la vez de un iterable, es decir
# de listas, conjuntos, tuplas... si todos son True devuelve True, sino False
# Por lo tanto, si hay al menos un False devuelve False
A = all(["Hola, que tal", 3, [1,5,8], "esto es una lista y dentor tiene otra"])
print(A)
print("-----------------------------------")
# Devuelve True, si tuviera alguna condición como las de bool() para False, devuelve False

# Función sum, suma todos los elementos de un iterable
numeros = [1, 3, 5] # Si hubiese strings, me devuelve error
S = sum(numeros)
print(S)
# También me daría error si tuviera una lista dentro de esa, o otro iterable dentro
print("-----------------------------------")

# Estas funciones, como dijimos ya fueron creadas
# ¿Pero cómo hacemos para crear las nuestras propias?
