# Existe otra forma de hacer una tupla y es con la función tuple()
tupla=tuple(["dato1", "dato2"]) # Se requieren los corchetes

# Otra manera
tupla = "dato1", "dato2" # Sin parentesis, ni nada, es lo mismo
# Si queremos crear una tupla con un sólo dato sin parentesis, debemos poner la coma luego del dato y listo
tupla="dato1",

# Recordar que la tupla es inmutables, a diferencia de la lista
print(tupla)

# En resumen, las tuplas son optimas para tener los datos fijos, sin correr riesgos de que sean alterados
# # Y las listas son para datos más flexibles