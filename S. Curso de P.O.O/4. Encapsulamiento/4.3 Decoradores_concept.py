# Es una función especial, que decora a otra
# Agrega un código extra,a uno que ya existía, antes o después
# Es decir la entrada es una función, y de salida es la función modificada

def decoradorr(funcion):
    # Crearemos una función decoradora, que no pedirá como argumento una función
    def fun_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Después de llamar a la función")
    return fun_modificada

# Lo que hace es ejecutar el código "Antes..." 
# Luego la función que le pasemos como argumento, y finalmente la útlima línea de código "Después..."

# def saludo():
#     print("Hola Dalto")

# # decorador(saludo) # Así no pasa nada porque tengo que asignarle una variable
# SM = decoradorr(saludo)
# SM()

# El principal uso de esto, es como les mencionaba, se puede agregar un código antes y después
# ctrl+k+c comento todo lo que selecciono
# Existe una forma más óptima de hacer esto y es:

@decoradorr 
def saludo():
    print("Hola Dalto")

# Con el @ le indicamos que creamos la función sobre el decorador
# Le estamos indicando a PY que debajo viene una función decoradora

saludo()

# También existen decoradores con argumentos, decoradores de clases (agregando antes o después cosas a la clase), de todo...
# Investigar