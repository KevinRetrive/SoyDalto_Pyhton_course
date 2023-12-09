# La función lambda se crea con el siguiente formato:
# "NOMBRE_FUNCION = LAMBDA PARAMETRO : EXPRESION"
potencia = lambda x : x**2
# Lambda crea funciones anónimas, es decir no almacenadas,
# Como cuando creamos una lista, o una cadena de texto, sin asociar a una veriable o nombre

print(potencia(3))
# Beneficios de usar esta función:
# No requiere crear un bloque de código
# Retorna automáticamente

print("----------------------------------------") 

# Función filter (building, porque está creada en python)
# Devuelve T or F, creando una lista para todos los elementos que son T
num=[1,2,3,4,5,6,7,8,9]
def es_par(numero):
    if(numero%2 == 0): 
        # "Si el resto de dividir por 2 es cero, OK"
        # Si quisiera los impares igualaría a 1
        return True

num_pares = filter(es_par,num) 
# Le aplica la función es_par a cada elemento de num
# Se agregan los True a una lista, mientras que los False no
print(list(num_pares))
# Pero para poder verlo bien en el worflow, convertimos en lista el argumento
    
print("----------------------------------------") 
# Creando lo mismo que antes pero con lambda    
num=[1,2,3,4,5,6,7,8,9]
pares = filter(lambda numero:numero%2 == 0, num)
print(list(pares))

