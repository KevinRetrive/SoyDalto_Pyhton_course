# Vamos a construir atributos o propiedades de instancia, para poder hacer una receta donde haya más de una marca por ejemplo
# Hay que sacarle los aprentesis y crear una función de un método especial llamado __init__()
# Pero lo que hará esta función que creamos, será que c/vez que instanciemos una clase, el método se ejecuta 
class Celular:
    def __init__(self, marca, modelo, camara):
     self.marca = marca  
     # Atento, con lo de la izq del igual creo la propiedad de self (podría haber puesto marca u otra cosa lo que sea) 
     # y con lo de la derecha accedo al parámetro de la función __init__ 
     # self se usa para decir que es el objeto mismo instanciado al que voy a llamar ahí
     # Es decir que si creo celular1, print(self.marca) es lo mismo que usar celular1.marca
     self.mod = modelo  
     self.cam = camara + " MP" # Podría agregar esto acá y no tener que cargarlo como atributo en el objeto
     
celular1 = Celular("Samsung","S23","48") 
# Le pasamos los atributos, y se denominan atributos d einstancia porque se los pasamos cuando creamos el objeto
print(celular1.cam)
celular2 = Celular("Apple","iPhone 15 pro","96")
print(celular2.cam)

# No nos olvidemos que un objeto se compone de dos cosas: Sus propiedades y las acciones que puede hacer
# Ya definimos sus propiedades, el cómo son (color, tamaño, etc), ahora veremos cómo definir sus acciones 
# denominadas métodos de los objetos y veremos en el siguiente archivo