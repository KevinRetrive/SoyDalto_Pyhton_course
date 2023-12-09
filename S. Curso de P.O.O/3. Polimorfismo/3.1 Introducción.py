# ¿Qué es? Es un concepto que hace referencia a poder enviarle un mensaje sintáctico a diferentes objetos bla bla
# De otra forma... basicamente es hacer, que cuando nosotros le demos un método a un objeto, 
# se comporte diferente entendiendo que sus propiedades son diferentes, le decimos al objeto que camine por ejemplo
# pero si creamos un objeto que es una persona, otro un gato y otro un perro
# todos caminaran pero diferente (mismo mensaje, con distintos resultaodos para objetos)
# Todas las variables en PY son polimorfas porque pueden tomar distintos tipos de datos, eso se llama polimorfimsmo en tiempo de ejecución o de inclusió
# Si yo creo una variable.. esta podría ser un string, o un numero, o lo que se le cargue

# Existen muchos tipos de polimorfismo = PM
class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"


# ¿Cómo aplica el PF acá? Bueno hay dos formas... Si creo un obj
gato = Gato()
perro = Perro()
print(gato.sonido())
print(perro.sonido())
# Acá tenemos PF de inclusión, el método no cambia, sino que el obj que lo antecede cambia (perro, o gato),
# y nos devuelve el mismo sonido.

def hacer_sonido(animal):
    print(animal.sonido())
hacer_sonido(gato)
hacer_sonido(perro)
# Acá tenemos otro PF de función, la función no cambia, sino que el argumento cambia (perro, o gato),
# y nos devuelve el mismo sonido.

# OBS en C++ o Java no se podrían crear métodos con el mismo nombre, a pesar de existir el PF, es decir que si o si para que
# tengan el mismo método se requiere que sean clases heredadas de otras clases, en PY no porque es de tipado DINÁMICO

# También tenemos el PF por herencia (aparecen los PF de subclases), sería lo mismo pero con clases que heredan el mismo método

# Existen otros, 
# como el de sobrecarga (overload), en una misma clase varios métodos con igual nombre pero con x distintos argumentos
# donde se ejecutara el que corresponda según la cantidad de argumentos que yo le ingrese a la hora de ejecutarse
# Pero en Y no existe este PF, para ello esta el comando args (lo vimos en el curso de PY)...

# O el PF de cohersión (en PY es automática, si tiene que sumar un int con un float, transforma el int automáticamente)
def recorrer(elementos):
    for item in elementos:
        print(f"El elemento actual es:{item}")

lista1=[1,3,5,7]
lista2="Huevon"
recorrer(lista2)
# No importa que la lista sea un str o un nro, las recorre igual, eso es PF

# Buscar info conceptual sobre duck typing, enlaces dinámicos/estáticos y tipos real/declarados

