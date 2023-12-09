# Creando una función que me devuelva los números primos
# entre el 0 y el argumento que le pasemos

def es_primo(num):
    for i in range(2,num-1): 
        # Debe ser a partir de 2 y hasta el anterior al num
        # porque sino dará de resto cero, ya que todos los n° son divisibles por 1 y por si mismos, dando resto 0
        # Y no deseo que esto me arroje True para 1 y para el mismo num
        if num%i == 0: return False
        # Si es divisible por alguni, retornamos False y termina el bucle
    return True
        # Si termina el bucle significa que no fue divisible por ninguno y entonces es primo
        # Recordar, que usar return, nos retorna directamente algo y a la vez funciona como un break, corta el bucle

# Ahora debemos crear otra función en donde llamamos a esta función que creamos:
def primos_hasta(num):
    primos = []
    for i in range(3,num+1): 
        # +1 para que nos tome el num incluido por si llegará a ser n° primo
        # Y a partir de 3 para que no comience y agregue al 2 en la lista
        resultado = es_primo(i) # Verificamos si es primo
        if resultado == True: primos.append(i) # Agregamos el n° primo a la lista
    return primos # Devolvemos la lista

# Creamos el resultado de la función y devolvemos la lista
resultado = primos_hasta(13)
print(resultado)

