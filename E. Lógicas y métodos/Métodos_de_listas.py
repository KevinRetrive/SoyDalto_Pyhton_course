# función list([dato0, dato1, dato2]) crea una lista
A = list(["hola", 5, 6, 7])
print(A)

# función len() devuelve la cantidad de elementos que posee la lista
print(len(A))

# método .append("jajaja") agrega elementos a la lista
# método .insert(índice 2 contando desde el 0 recordar, "jajaja") agrega elementos a la lista en una posición espécifica
# método .extend(["jajaja", 3.5, "bai"]) agrega una lista a la otra lista
# método .pop(n° del índice por ej 0) elimina un elemento de la lista según el índice indicado, obs con el -1 le indicamos que elimine el último, el -2 el ante-último y así
# método .remove(valor) remueve un elemento por su valor, es decir hay que escribirlo exactamente igual
# método .clear() elimina todos los elementos
# método .sort() ordena de manera ascendente la lista siempre y cuando no haya cadenas de texto salvo True or False. Si insertamos .sort(reverse=True) los ordena de manera descendente.
# método .reverse() invierte los elementos de una lista, si antes la ordenamos con sort, llegamos al mismo resultado

# También hay otros comandos. Y para las tuplas (listas con parentesis) se utlizan distintos métodos y algunos similares, ver con la función dir
# Recordar que en las tuplas y los conjuntos no se las puede cambiar, modificar, reverir por lo que la mayoría de los métodos son para contar, hallar