# El desempaquetamiento es, la creación de variables nuevas tomando datos de por ejemplo una tupla
# Creamos una tupla
# Funciona con listas, y conjuntos también

datos_tupla=("Alfredo","Machi")
datos_lista=["Alfredo","Machi"]
datos_set={"Alfredo",300} # Para conjuntos no me permite desempaquetar n° OJO

abuelo,abuela=datos_tupla # Se debe tener igual n° de variables que de datos
abuelito,abuelita=datos_lista
abuelucho,abuelucha=datos_set
print(abuelucho)
print(abuelucha) # Igual si me dejó el set desempaquetar el n°, pero weno
