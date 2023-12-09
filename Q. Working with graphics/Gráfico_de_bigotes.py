# Y queremos graficar una recta de fecha y cantidad de pedos que me tiro por día
# Creamos el archivo CSV "pedos" con 2 columnas fecha,pedos
import pandas as pd

# Vamos a usar la librería de Python de visualización de datos
import matplotlib.pyplot as plt
# Lo instalamos en el CMD de la pc "py -m pip install matplotlib"

# Y una librería de graficos estadisticos
import seaborn as sns
# Lo instalamos en el CMD de la pc "py -m pip install seaborn"

# Ahora leemos el CSV como dataframe
df = pd.read_csv("18. Working with graphics\\Bigotes.csv")
print(df)

# Creamos un grafico de lineas con sns.scatterplot(x="" , y="",data=df)
sns.boxplot(x="Categoria",y="Valor",data=df)
# Lo que hacemos al colocar el 3er argumento "data=df" es que busque en el CSV
# esas columnas y traiga los valores por eso debo escribir tal cual x e y

# Ahora mostramos el gráfico con plt.show()
plt.show()


# OBS: La línea 14 si bien esta bien usarla, no es la mejor opción para cargar grandes base de datos
# Para archivos con muchos datos se recomienda cargarlos de la siguiente manera
# En vez de pd.read_csv:
#def read_csv_in_chunks(file_name):
#    for i, chunk in enumerate(pd.read_csv(file_name,chunksize=1000)):
#        print("Chunk #{}".format(i))
#        print(chunk)
#read_csv_in_chunks("big_file.csv")

# O también
#import csv

#def read_csv_in_chunks(file_name):
#    with open(file_name,'r') as f:
#        reader = csv.reader(f)
#        header = next(reader)
#        for i, chunk in enumerate(reader):
#            print("Chunk #{}".format(i))
#            print(chunk)
#read_csv_in_chunks("big_file.csv")