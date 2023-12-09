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
df = pd.read_csv("18. Working with graphics\\cofla_ingresos.csv")
print(df)

# Creamos un grafico de lineas con sns.barplot(x="" , y="",data=df)
sns.barplot(x="Fuente",y="Ingresos",data=df)
# Lo que hacemos al colocar el 3er argumento "data=df" es que busque en el CSV
# esas columnas y traiga los valores por eso debo escribir tal cual x e y

# Pero queremos que además muestre el total de todo, usamos el siguiente método
total = df['Ingresos'].sum() # Nos suma todos los valores de la columna indicada
print(f"El total de ingresos es de: ${total} USD")

# Ahora mostramos el gráfico con plt.show()
plt.show()

