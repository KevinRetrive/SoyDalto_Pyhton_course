# DIP: dependency inversion principle
# Basado en que:
# Los módulos de alto nivel no deben depender de los de alto nivel, sino que los dos deben depender de las abstracciones
# Y las abstracciones NO deben depender de los detalles, sino que al revés

# En otras palabras, no tenemos que depender de implementaciones especificas (como funciones o códigos específicos),
# sino de algo complejo que abarque todo lo posible, una clase o módulo de mayor magnitud
# para que de esta forma las clases de más alto nivel (que contienen las lógicas) se mantengan independiente de las de bajo nivel (que realizan funciones esp.)

#Ej:
# Imaginemos que creamos un procesador de texto

# class Diccionario():
#     def verif_palabra(self,palabra):
#         # Lógica para verificar palabras
#         pass
    
# class CorrectorOrtografico():
#     def __init__(self):
#         self.dicc = Diccionario()
#         # Va a tener un objeto del tipo Diccionario() con todas sus lógicas
    
#     def corregir_txt(self,texto):
#         # usamos el diccionario para corregir

# El problema de esto es que CorrectorOrtografico() esta fuertemente ligado al Diccionario()
# Porque aunque acá no lo veamos, los métodos que tengamos en Diccionario() deben replicarse en corregir_txt()
# Tq si modificamos Diccionario() porque se halló una lógica mejor en otro libro deberíamos también cambiar el código en corregir_txt()
# De manera que no es óptimo, el corrector depende del diccionario, y se esta violando el principio de independencia
# Además corrector es el código más complejo, y que tiene nuestro desarrollo, el diccionario sólo cumple una función y es una herramienta, no tiene sentido que corregir depende de éste

# Manera correcta de hacerlo. Comento todo lo anterior. Ej

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabras(self, palabra):
        # Lógica para verificar palabras
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabras(self, palabra):
        # Lógica para verificar palabras si es que está en el diccionario
        pass
    
class DiccionarioOnline(VerificadorOrtografico):
    def verificar_palabras(self, palabra):
        # Lógica para verificar palabras online
        pass
    
class CorrectorOrtografico:
    
    def __init__(self,verificador):
        print("")
        # usamos el verificador para corregir el texto
        
    def corregir_texto(self,texto):
        print("")
        # usando el verificador para corregir texto
        
# Explicación
# Ahora el CorrectorOrtografico() está dependiendo de la interfaz abstracta del VerificadorOrtografico (que puede ser Diccionario u otro),
# y el verificador, se encarga de verificar el diccionario
# Nuestro corrector YA NO depende del diccionario,
# esto significa que podemos cambiar de diccionario sin problemas en nuestro código

# Como verificador es una clase abstracta tenemos todos los métodos que necesitamos ahí mismo, si aparecen más metodos en los diccionarios, 
# podemos quedarnos tranquilos de que podemos seguir usando los mismos métodos que tenga el verificador, porque al ser una subclase tendría
# que poder hacer todo lo que hace la clase base (Principio 3 de Liskov)

# Cualquiera de ambas es válida por lo explicado
# corrector = CorrectorOrtografico(Diccionario())
# corrector2 = CorrectorOrtografico(DiccionarioOnline())

# OBS: No siempre es fácil aplicar todos los principios, hay excepciones o sesgos, pero la idea es hallar el óptimo
