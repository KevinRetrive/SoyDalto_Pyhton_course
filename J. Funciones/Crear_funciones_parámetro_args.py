# Forma no óptima de sumar valores de una lista

def suma(lista): # Creamos una función con dos argumentos
    num_sumados=0
    for numero in lista:
        num_sumados = num_sumados + numero
    return num_sumados

resultado = suma([5,3,9,100])
print(resultado)
# PERO deberíamos hacer que la cantidad de argumentos que le pase sea indefinida,
# esto no es óptimo, no pasar una lista, sino que:

# Forma óptima = utilizando el parámetro args "*"
def suma(nombre, *numeros): 
    # Lo que hace el asterisco es decirle que esos argumentos serán una lista
    # Si agrego más parámetros, el que contenga al asterisco debe ir al final, por ej. agrego el parámetro nombre
    # Porque después de la primer coma el argumento considera que todos son pertenecientes a la lista números,
    # y si agrego más nunca sabrá cuando es el que le corresponde porque para números corresponden infinitos
    return f"{nombre}, la suma de tus n° es {sum(numeros)}"
    # Recuerden que la función sum() realiza la suma de todos los elementos de un iterable
    
resultado = suma("Kevin", 5,3,9) # No preciso ponerlos como una lista
print(resultado)

# También existe la posibilidad de no usar el args como parámetro:
def suma(numeros): 
    return sum(*numeros) 
# Y lo usamos acá, le decimos que será una lista
# La ppal ventaja de esta forma, es que podemos agregar parámetros sin problemas,
# Ya que, si bine la forma anterior es la mejor, si o si el argumento con args debe ir último

