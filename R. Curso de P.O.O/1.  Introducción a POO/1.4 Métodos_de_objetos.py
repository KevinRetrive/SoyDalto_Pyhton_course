# Un método es una función, la diferencia es que si creamos una función con "def" pero la insertamos dentor de una clase, pasa a llamarse método
# Y además debemos instertar el parámetro self dentro del parentesis por convertirse en un método de una clase

class Celular:
    def __init__(self, marca, modelo, camara):
     self.marca = marca  
     self.mod = modelo  
     self.cam = camara + " MP"
     
    def llamar(self):
        print(f"Estas haciendo un llamado desde un: {self.mod}")
    def cortar(self):
        print(f"Estas terminando un llamado desde tu: {self.mod}")

     
celular1 = Celular("Samsung","S23","48") 
celular2 = Celular("Apple","iPhone 15 pro","96")

celular1.llamar() # No preciso usar print para llamar al método
celular2.cortar()

# OBS s epreguntaran por __init__, es un método constructor especial que nos permite definir muchas cosas, 
# principalmente las propiedades que son parte del objeto