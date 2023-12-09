"Con F5 ejecuto el RUN"
"Dos formas de hacer una operación antes y después del igual"
"Si lo hago antes del igual reconoce el último valor de la variable nombre"
nombre = 10
nombre = 10 + 1
nombre += 5

print(nombre)

"Para convertir una variable en texto y poder concatenar uso la función f al incio ejemplo:"
"Con las llaves dejo afuera de las comillas la variable nombre para que la inserte allí"
"Es la mejor opcion siempre usar el fstrings para evitar problemas con textos y numeros combinados"
#Variable con CamelCase
NombreApellido= 5
#Variable con snake_case
bienvenido_al_programa= f"Hola {nombre} ¿cómo estás?"
print(bienvenido_al_programa)
#A cada variable se le asigna un dato

"El comando del al inicio sirve para borrar del código una variable (me dará error si lo corro)"
del nombre 
"no afectara al print bienvenida porque ya se creó"


"print se puede usar para buscar tipos de datos (strings o nros, etc) en las variables ej:"
print("Hola" in bienvenido_al_programa)
#Y devuelve true or false, son operadores de pertenencia in/not in
#Así realmente se comenta, lo naranja en realidad es texto, son datos.