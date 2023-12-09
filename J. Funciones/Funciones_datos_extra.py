
def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

rta = frase("flor", "hueche", "hermosa")
# Ahora, si el usuario quiere ingresar 1ero el apellido, el sistema me devolvera 1ero el apellido, ¿Puedo invertir el orden en los argumentos?
# Si se puede, se los puede forzar de la siguiente manera:
rta = frase(adjetivo= "hermosa", nombre="flor", apellido= "hueche")
print(rta)

# O incluso se puede usar como constante en los parámetros, y no usar keyword arguments
# Por ej:
def saludo(nombre= "florcita",apellido= "hueche",adjetivo= "hermosa"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

# Pero esta función posee parámetros constantes, no import lo que ingrese como argumentos, siempre devuelve lo asignado
rta2=saludo("Flor","Agustina","linda") # En realidad ni requiere argumentos
print(rta2) # Aunque podemos cambiarlos si agregamos los argumentos

