# Es una función que nos permite pedirle un dato al usuario, denominamos esto como input
nombre=input("Capo, ¿cómo te llamas?: ") # la función input es para devolver datos tipo textos OJO, si pongo un n° lo tomará como texto
# Si deseamos mostramos el dato
# print(nombre)
# O mejor aún podemos concaternarlo con algo que deseemos
print(f"El nombre es: {nombre}")

# Si insertara un n° y lo multiplco por 2... sólo se repetira el caracter dos veces porque es texto
# Sin embargo puedo convertirlo en n° y solucionado:

edad=input("¿Cuántos años tenes?: ") # Si multiplicara por 2 acá me devolvería 2626
respuesta=int(edad)*2
print(f"Su edad es: {respuesta}")

# Puedo hacer lo mismo y convertirlo a un número no entero, con la función float
# Si se que el usuario puede ingresar un n° float, debo trabajar con float, sino me tirará error la función int