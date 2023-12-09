# ISP: interfaz segregation principle
# Basado en que ningún cliente tiene que ser forzado a ser dependiente de interfaces que no utilice
# es decir, se deben eliminar las dependencias que no vamos a usar

# OBS: Interfaz = Clases abstractas
# Supongamos que tenemos que definir una interfaz para un trabajador con métodos para comer,dormir y trabajar:
# Y que hay dos tipos de trabajadores (subclases)

from abc import ABC, abstractmethod

# class Trabajador(ABC):
#     @abstractmethod
#     def comer(self):
#         pass
    
#     @abstractmethod
#     def trabajar(self):
#         pass

#     @abstractmethod
#     def dormir(self):
#         pass

# class Humano(Trabajador):
#     def comer(self):
#         print("El humano esta comiendo")
    
#     def trabajar(self):
#         print("El humano esta trabajando")

#     def dormir(self):
#         print("El humano esta durmiendo")

# class Robot(Trabajador):   
#     def trabajar(self):
#         print("El robot esta trabajando")

# robot1 = Robot()
# Vemos que al crear un objeto para la subclase Robot() me tira error, 
# ya que necesita el método comer y dormir
# Estoy obligado a definir estos métodos en Robot()?
# Okey estoy dependiendo de una interfaz (clase padre) que no uso
# Yo podría poner esos metodos y poner pass... pero está mal conceptualmente, estaríamos violando el principio

# La forma correcta es dividir la interfaz, en interfaces más pequeñas hasta que se respeten entre sí
# Es decir, la clase padre Trabajador() no debería incluir a comer y dormir porque no tienen nada que ver con ello
# ya que no todos los trabajadores comen y durmen
# Se relaciona también con el 1er principio pero aquí la diferencia reside en la plantilla o interfaz inicial que queremos dejar fija

# Comento todo y realizo esto de la manera correcta respetando el principio:

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comensales(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmientes(ABC):
    @abstractmethod
    def dormir(self):
        pass

# Ahora las subclases deben heredar de estas 3 y deben tener sus métodos, o los que deseemos
class Humano(Trabajador,Comensales,Durmientes):
    def comer(self):
        print("El humano esta comiendo")
    
    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):   
    def trabajar(self):
        print("El robot esta trabajando")

robot1 = Robot()
humano = Humano()
robot1.trabajar()
humano.trabajar()
