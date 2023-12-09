import pandas as pd
df = pd.read_csv("C:\\Users\Kevin\OneDrive\Escritorio\Pyhton\\17. Ejercicios prácticos 3\\Data.csv")
# print(df) cheque el data frame

# Tarea, cambiar el tipo de dato de una columna con el método .astype()
df["Edad"] = df["Edad"].astype(str)
# print(df["Edad"][0]) # Que me escriba el 1er elemento de la columna edad
print(type(df["Edad"][0])) # Que me escriba el tipo de dato del 1er elemento de la columna edad
# Se puede ver que ya no dice más que es un numpy.int (entero) sino un str (string)

# Reemplazando un dato (o cada vez que se repite) por otro con el método .replace()
df["Nombre"].replace("Agus","Agustina",inplace=True)
print(df["Nombre"])

# Que pasa si los datos tienen filas con datos faltantes, como las eliminamos? con el método .dropna()
# df_sin_filas_con_datos_faltantes = df.dropna(), 
# si le ingresamos "axis=1" como argumento, se borrarian las columnas con datos faltantes
# No lo hice porque tenía que editar el CSV y ni ganas

print("---------------------------------------")
# Otra cosa que podemos hacer, es eliminar filas repetidas con 
df_corregido = df.drop_duplicates()
print(df_corregido)

print("---------------------------------------")
# Surge un nuevo problema, como haríamos para guardar este nuevo archivo modificado como CSV?
# Recreamos un CSV con el df resultante
df_corregido.to_csv("17. Ejercicios prácticos 3\\Data_clean.csv")
