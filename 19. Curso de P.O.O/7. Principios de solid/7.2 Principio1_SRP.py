# SRP: Single rsponsability principle

# Se basa en que una clase tiene que tener una, y sólo una, razón para cambiar
# Cada clase tiene que tener una única responsabilidad o tarea

# Por ej: Sería una mala práctica tener una clase autos con funciones como bombear aceite al motor, encender luces, 
# manipular los limpia parabrisas, etc. Ya que si falla algo, falla todo por ejemplo.

# Con este principio, se evita que los desarrolladores creen clases sobre-cargadas, o complejas (multi-funciones), poco legibles
# Además la clase puede funcionar independientemente de las demás, ya que cumple una función única
# Ej:

#class aaaaAuto():
#    def __init__(self):
#        self.posicion = 0
#        self.combustible = 100
        
#    def mover(self, distancia):
#        if self.combustible >= distancia/2:
#            self.posicion += distancia
#            self.combustible -= distancia/2
#        else:
#            print("No hay suficiente combustible")
    
#    def agregar_combustible(self,cantidad):
#        self.combustible += cantidad
        
    # Recordamos, esto es un getter, estamos obteniendo el combustible
#    def obtener_combustible(self):
#        return self.combustible

# En esta clase, no se respeta el principio, ya que ésta se encarga del traslado del auto
# y a su vez del combustible, en la vida real no sería práctico, 
# la manera correcta sería hacer otra clase para el combustible

class TanqueCombustible:
    def __init__(self):
        self.combustible = 100 
        # Todos los tanque que creemos tendrán esta propiedad estática que son 100 disponible para gastar
        
    def agregar_combustible(self,cantidad):
        self.combustible += cantidad
        # con el += le agregamos a la cantidad que tenemos actual, más combustible
        
    def obt_comb(self):
        return self.combustible
    
    def usar_comb(self,cantidad):
        self.combustible -= cantidad


class Auto():
    def __init__(self,tanque):
        self.posicion = 0 # Atributo estático
        self.tanque = tanque # Atributo de instancia, le debemos ingresar un objeto
        
    def mover(self,distancia):
        if self.tanque.obt_comb() >= distancia / 2: # SI el combustible actual es suficiente.. que haga lo siguiente
            self.posicion += distancia # Que se actualice la posición
            self.tanque.usar_comb(distancia / 2) # Que se consuma el combustible indicado
            print("Has movido el auto exitosamente")
        else:
            print("No hay suficiente combustible")
            
    def obtener_pos(self):
        return f"La posición actual es: {self.posicion}"

# 1ero creamos un tanque
tanque = TanqueCombustible()
# Y un auto con ese tanque
autito = Auto(tanque)

print(autito.obtener_pos())
autito.mover(10)
print(autito.obtener_pos())
autito.mover(20)
print(autito.obtener_pos())
autito.mover(60)
print(autito.obtener_pos())
autito.mover(100)
print(autito.obtener_pos())
autito.mover(100)
print(autito.obtener_pos())

# OBS: ME DA NONE SI USO PRINT CON MOVER() YA QUE YA TIENE UN PRINT,
# EN CAMBIO OBTENER_POS USA RETURN !!! MIERDA

# Esta es la forma óptima de respetar el primer principio.