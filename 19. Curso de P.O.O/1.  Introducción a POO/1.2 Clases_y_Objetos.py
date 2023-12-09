cel1_marca = "samsung"
cel2_marca = "apple"
cel3_marca = "huawei"

cel1_modelo = "S23"
cel2_modelo = "iPhone 15 pro"
cel3_modelo = "P20 pro"

cel1_camaraT = "48 MP"
cel2_camaraT = "48 MP"
cel3_camaraT = "12 MP"

cel1_camaraF = "24 MP"
cel2_camaraF = "24 MP"
cel3_camaraF = "8 MP"

# Fijemosnos que creamos un monton de variables con sus respectivas propiedades
# Pero sería muy tedioso recurrir con un print() a cada una de ellas usando líneas de códigos
# O también podría haber hecho un array con la info para cada celular, pero estamos en la misma
# No es práctico, ni reutilizables, ni óptimo
# ¿Cómo podemos hacer esto de una manera más óptima?

# Clase = "Receta para crear objetos, definir sus caracteristicas, propiedades" y se crea con "class"
# y la palabra siguiente, para definir el nombre de una clase, como snake_case (separadas por guiones) o 
# camelCase (1er letra de 1er palabra en minúscula y el resto de las 1eras letras de las otras palabras en Mayúscula) o 
# PascalCase (igual que el anterior pero la 1er letra es mayúscula en vez de minúscula), la más usada

class Celular():   # Nombre de la clase
    # propiedad1 = "valor 1"
    # propiedad2 = "valor 2"
    # propiedad3 = "valor 3"
    # Estos se denominan atributos estáticos porque para todos los objetos van a ser iguales
     marca = "Samsung"
     modelo = "S23"
     camara = "48 MP"

# Un objeto es la instancia de una clase (podría crear "infinitos" objetos dentro de una clase)
# En este caso sería útil si yo quisiera usar esta receta en una fabrica para producir masivamente este cel
# Crearíamos el objeto así:
celular1 = Celular()
celular2 = Celular()
celular3 = Celular()
celular4 = Celular()

# Cuando creamos un objeto, es información que se almacena en la RAM (es decir, se elimina tras cerrar el programa)
print(celular1) # Vemos que nos dice que es un objeto, pero no nos da valores, para ver sus caract. es así:
print(celular1.marca) # Es la forma de preguntarle las propiedades al objeto celular1 que creamos
# Si colocara cualquiera de los otros 3 celulares creados también me darían la misma respuesta porque los creamos bajo la misma clase
# Podría decirle al código que celular1.marca = iPhone y cambiarle el atributo por fuera de la clase

# "instanciar la clase" = objeto o crear objeto
# Sin embargo, existen otros tipos de atributos que no son estáticos, lo vemos en el siguiente archivo: Atributos
