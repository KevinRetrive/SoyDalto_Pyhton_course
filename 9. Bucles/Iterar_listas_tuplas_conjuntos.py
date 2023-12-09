# En Pyhton el FOR es FOR IN, lo que hace es crear una variable que en cada vuelta va a ser
# igual a ese pedacito de variable que estamos igualando, y se utiliza de la siguiente forma
# for VARIABLE in LISTA/TUPLA/CONJ :
# ¿A qué va a ser igual la variable? Va a ser la variable que va a ir igualando elemento a elemento y ejecutando el código
# Si hacemos print de la variable y por cada vuelta devuelve el valor de el elemento que corresponde

animales = ["gato", "perro", "loro", "cocodrilo"]
for animal in animales:
    print(f" Ahora la variable animal es: {animal}")

# Otro ejemplo recorriendo la lista numeros y afectandola x10
numeros= [12 ,24 ,36, 48]
for numero in numeros:
    resultado = numero*10
    print(resultado)
    
# Si quisieramos recorrer dos listas, podemos anidar los for in, e ir trabajando con dos variables
# Otra opción es utilizar "zip", que nos permite recorrer dos listas al mismo tiempo 
# Para poder realizar esto las listas deben tener IGUAL cantidad de elementos
# Se codifica así
for numero,animal in zip(numeros,animales):
    print(f" Recorriendo lista 1 el animal es: {animal}")
    print(f" Recorriendo lista 2 el n° es: {numero}")
# Si alguna de las listas tuviera más elementos que la otra, no tira error, pero el bucle se frena en la lista
# que posea menor cantidad de elementos y no veríamos el resultado de los elementos restantes de la otra lista
# zip sirve para 2 o más listas al mismo tiempo

# Otra opción para iterar es usando la función range
for num in range(5,10): # El primer argumento es de donde arranca la variables y el segundo hasta donde
    print(num)
    # Se puede ver que comienza en el primer argumento y termina en el elemento anterior al último, es decir el último no lo recorre OJO
# OBS si sólo le ingresamos un argumento, comienza de 0 por defecto

# Otra forma NO óptima de recorrer una lista:
#for nume in range(len(numeros)):
#    print(numeros[nume])
# Esta forma no funciona en conjuntos!

# Otra forma SI optima de recorrer la lista es con la función enumerate()
for nu in enumerate(numeros):
    print(nu) # Nos devuelve el índice y su valor
# Si sólo queremos acceder al indice colocamos print(nu[0]), y si sólo al valor un 1
# O incluso a ambos:

for n in enumerate(numeros):
    indice=n[0]
    valor=n[1]
    print(f"EL índice es: {indice} y el valor es: {valor}")
    
# OBS al usar enumerate, n pasa a ser una tupla!

# Nos desafia a desempaquetar la tupla directamente en el for
for numer in enumerate(numeros):
    ind,val=numer
    print(f"índice: {ind} - Valor: {val}")
else:
    print("El bucle terminó")
# Lo hice, perfecto
# El else siempre se muestra sólo al final del bucle, sólo una vez 
# y siempre si o si se muestra, a menos que haya un break, que veremos más adelante
# Todo lo visto funciona exactamente igual si hubieramos tenido tuplas o conjuntos en vez de listas
