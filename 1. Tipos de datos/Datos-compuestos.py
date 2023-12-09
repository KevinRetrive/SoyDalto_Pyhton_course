#Los datos complejos son datos, con datos dentro, y así

#El primer tipo es: La lista
lists = ["Hola", True, 5, 2.4]
print(lists)
#Si quiero que solo me de un dato de la lista, debemos recordar que cuenta del elemento 0 al 9
print(lists[0])

#El 2do tipo son las tuplas, iguales a las listas pero usando parentesis
tupla=("Hola", True, 5, 2.4)
print(tupla[0])
#Sin embargo, las tuplas no se pueden modificar en otra linea tras ser creadas
#tupla[2] = verdadero
# #print(tupla[2]) da error porque no se puede modificar, pero la lista si ej:
lists[0]="Chau"
print(lists[0])

#El 3er tipo es el conjunto (set)
conjunto = { "Hola", True, 5, 2.4 }
#Se puede re-definir o re-construir en otra linea (en la tupla igual)
conjunto = { "Así", "Jaja" }
#Pero no editar un elemento en una línea, al igual que las tuplas
#Así conjunto[1]="jajajaaja" recordar que es de 0 al 9 los elementos, entonces el 1 es el que era "jaja" antes
#Pero no me permite imprimir por indice, así print(conjunto[1]), si o si debo imprimir todo el conjunto
#A diferencia de la lista y la tupla, el conjunto no permite tener elementos repetidos, así conjunto = { "Jaja", "Jaja" }
#Sirve entonces para eliminar duplicados
#Como no se puede acceder a su índice, este trabajo reuiere un bucle, lo que veremos más adelante


#El 4to tipo es el diccionario (dict), no define automaticamente los elementos del 0 a 9
#Especie de lista, en el que nosotros nombramos a los elementos, por ej. en este caso el elemento 0 es nombre
diccionario= {
    "Nombre": "Kevin",
    "Edad": 26,
    "Altura": 1.8,
    "Edad": 26,
    "Sexo": "M",    }
print(diccionario["Altura"]+10)
#Puedo operar dentro de la impresión (suma, resta, etc)
