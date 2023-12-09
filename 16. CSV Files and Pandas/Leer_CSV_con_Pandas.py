# Universalmente se reduce Pandas como pd
# Y si deseamos trabajar con esta librería hacemos lo siguiente:
# Escribimos cmd en el buscador de nuestra compu de windows, 2do click ejecutar como admin

import pandas as pd
print(type(pd))

# Para abrir un archivo lo hacemos de la siguiente manera, como hemos aprendido
archivo = pd.read_csv("16. CSV Files and Pandas\\Datos.csv",names=["name","surname","age"])
# Podemos modificar el encabezado como vemos arriba agregando un 2do argumento de esa manera con "names=[]"

# Colocamos la libreria Pandas "pd" luego el método .read_FORMATODELARCHIVO("NOMBRE DEL ARCHIVO")
print(archivo) # Me muestra todo, pero vemos que como le ingrese el argumento de un nuevo encabezado,
# los que habia escrito en el .txt me los pasa a datos y por lo tanto no me sirve en realidad así en este caso

print("------------------------------------------------------------------------------------------")
# Si quisiera ordenar por edad uso el método .sort_values("columna que quiero ordenar"):
ordenado = archivo.sort_values("age",ascending=False)#2do argumento indica cómo (Este caso de mayor a menor)
print(ordenado)

# o puedo pedirle que me muestre los datos se una sola columna como "nombre" por ejemplo:
# print(archivo["Nombre"])

# Esto que llamamos "archivo" en realidad se denomina data frame "df"
# El df son estructura de datos similares a una hoja de calculos (filas,columnas), no se comporta como un archivo común

print("------------------------------------------------------------------------------------------")
# También podemos concatenar 2 data frames, por ejemplo si abro otros 2 archivos más (copio y pego con otro nombre), 
# usando el método .concat() que es un módulo de pandas (pd) es:
df = pd.read_csv("16. CSV Files and Pandas\\Datos.csv")
df2 = pd.read_csv("16. CSV Files and Pandas\\Datos.csv")
df_concatenado = pd.concat([df,df2]) # Se le argumenta una lista con elementos que queremos concatenar
print(df_concatenado)

print("------------------------------------------------------------------------------------------")
# También tenemos las acciones .head() y .tail()
# Accediendo a las primeras dos filas
fila2 = df.head(2) 
# Me mostrará la fila 1, con el 0 me devuelve el encabezado, si ingreso un 2 me mostrará las primeras 2 filas, y así
print(fila2)
# .tail() funciona exactamente igual pero desde la última fila
print("------------------------------------------------------------------------------------------")

# ¿Cómo accedemos a la cantidad de filas/columnas si no las conocieramos? Con shape
# shape es un atributo, es como una variable de un objeto
filas_columnas_totales = df.shape
print(filas_columnas_totales) # Nos devuelve "(n° filas, n° columnas)", es decir, en forma de tupla
# Entonces si tengo estos valores podría desempaquetarlos:
filas,columnas = filas_columnas_totales[0],filas_columnas_totales[1]
print(f"Tengo {filas} filas")
print(columnas)
print("------------------------------------------------------------------------------------------")

# Otra función muy utilizada en análisis de datos para obtener data estadistica del dataframe es .describe()
df_info = df.describe()
print(df_info)

print("------------------------------------------------------------------------------------------")
# Métodos .loc[] y .iloc[]
# Accediendo a un elemento específico del df con loc
elemento_especifico_loc = df.loc[2,"Edad"] # Argumentos: fila 2 columna edad
# Accediendo a un elemento específico del df con iloc
elemento_especifico_iloc = df.iloc[2,2] # Argumentos: fila 2 columna 2
# Accediendo a todos los elemento del df de una sola columna con iloc
apellidos = df.iloc[:,1] # Argumentos: filas todas columna 1
print(apellidos)
print("------------------------------------------------------------------------------------------")
# Accediendo a todos los elemento del df de una sola fila con loc o iloc
Datoss = df.loc[2,:] # Argumentos: fila 3 columnas todas
print(Datoss)
print("------------------------------------------------------------------------------------------")
# Podría usarlo aplicando una condición por ejemplo accediendo a filas con edad > 30
mayores = df.loc[df["Edad"]>30,:] # Le indicamos sólo filas en las que Edad sea > 30 y columnas todas
print(mayores)
print("------------------------------------------------------------------------------------------")


# Podríamos trabajar con Jupyter Notebook, para hacerlo de manera óptima
# Es la forma óptima de trabajar con la ciencia de datos!
# Presionamos CTRL+SHIFT+P y escribo Create Jupyter Notebook y pasó todo el código ahí
# Lo corro y nos pedirá instalarlo, le damos OK y seguimos en esa hoja

