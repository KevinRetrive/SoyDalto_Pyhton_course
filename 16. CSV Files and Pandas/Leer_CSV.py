# De igual manera que los .txt :

import csv

with open("16. CSV Files and Pandas\\Datos.csv") as data:
    print("Data leida correctamente?")
    # print(data.read()) PERO no se usa así para estos archivos, 
    
    # sino que importamos el archivo csv y lo hacemos así:
    # print(csv.reader(data)) o de una manera para recorrer fila por fila:
    
    reader = csv.reader(data)
    for row in reader:
        print(row)
        # Y así convertimos las filas en listas, como se puede ver tneemos un 4to valor vacío, 
        # es porque pusimos una coma al final de cada fila en el .csv tal que las sacaremos
        
# Lo ideal es usar la librería de Py, Pandas que sirve para hacer esto de manera óptima
