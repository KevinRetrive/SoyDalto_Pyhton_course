# El encapsulamiento consiste en proteger los elementos de una clase (variables, métodos)
# Por ejemplo, que otro desarrollador no pueda ingresar a la clase que determina la contraseña del Facebook

# Hay dos formas de trabajar

# Una son los modificadores de acceso, en PY no existen, private y public, o sea si existen pero 
# no se dicen de esa forma, y no son completamente privados como tal, mm cualquiera puede acceder
# pero podemos convertirlos o darles aún más privacidad
# Ej

class MiClase:
    def __init__(self):
        # La forma de crear un atributo privado es colocando un guion bajo "_" al inicio
        # Para hacerlo aun más privado, le colocamos dos guiones bajos
        self.__atributopriv = "valor"

    def __hablar(): # De la misma forma puedo crear un método privado
        print("Holaa")
        
obj = MiClase()
# print(obj.__atributopriv)
# Y ahí nos tira error porque nos dice que es un atributo privado, es decir que no se accede como con un sólo guión
# De todas maneras, no es absolutamente privado, podemos acceder de una forma más compleja que no veremos

# El privado de PY es como el protegido de otros lenguajes, y el muy privado es como el privado

# ¿Ahora para que carajos usamos esto? 
# Mejora la legibilidad del código, el mantenimiento y la evolución, ya que al ser privados se acceden de otra forma

# ¿Cómo acceder a los atributos muy privados?
# Debemos usar getters (acceder a atirbutos privados o MP) y setters (Modificar o establecer atributos P o MP)
# Estos getters y setters son diferentes según querramos acceder a un método o a un atributo

# Lo mismo aplica para métodos privados, asi que creamos en la clase de arriba uno
# print(obj.__hablar()) y me da error porque esta como MP

