# OCP: Open/Closed principle
# Se basa en: Open for extension, closed for modify
# En definitiva siginifica que deberíamos porder agregar nuevas funcionalidades,
# sin modificar/afectar las que ya existen (el código fuente)

# Ej:
# Imaginemos un sistema que le envía notificaciones a los usuarios

class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario 
# Así como a Auto() le pasamos el objeto tanque, aquí, también deberían ser objetos,
# pero se volvería muy complejo y largo para explicar, pero un usuario ya tendría un email asociado,
# para que se entienda a donde quiero llegar
        self.mensaje = mensaje
        
    def notificar(self): # ¿Qué va a hacer esta función?
        raise NotImplementedError
# Con esto de acá, le estamos diciendo al código que tenemos que crear notificar, sirve para no andar modificando
# todo el tiempo, ya que podemos meter todas las funcionalidades allí pero si surge una app nueva que notificar,
# deberíamos andar modificando la función notificar todo el tiempo, entonces...
# supongamos que queremos notificar por correo electrónico, bueno para ello creamos una sub-clase que heredé de ésta

class NotificadorEmail(Notificador):
    def Notifica(self):
        print(f"Enviando mensaje por mail a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def Notifica(self):
        print(f"Enviando SMS a {self.usuario.SMS}")

class NotificadorTw(Notificador):
    def Notifica(self):
        print(f"Enviando mensaje por Twitter a {self.usuario.Twitter}")


# Usuario debería ser un objeto con email, n° de cel (SMS), etc.
# OBS: entonces de esta manera, si yo quiero agregar más funcionalidades, no tengo que editar la clase padre
# Sino que agregar una sub-clase, y en el caso que precise un dato que el usuario no tenga porque surje una app nueva
# como wsp, le indico al usuario que me pase su wsp y listo

# OBS2  RECORDAR
# Este no es un priincipio para que la clase no tenga muchas funciones... en eso se basa el 1er principio
# Este se fundamente en que se pueda extender la funcionalidad del principio sin modificar el código base

