import re
text = "The quick brown for jumps over the lazy dog"

x = re.search("^The.*dog$",text)
# 1ero ^ le indica que busque la cadena The al inicio de la linea
# 2do el . le indica que encuentre cualquier cosa que no sea un espacio de linea
# 3ero el asterisco es uno que no vimos, y lo que hace es lo siguiente:
# Le indica que a la primer tarea que tenga a la izquiera... si no halla nada en la busqueda, que lo deje pasar por alto,
# que no hay drama pero que si encuentra al menos un caracter de esos, que busque todos los que hay
# 4to $ le indica que busque la cadena dog al final de la linea
# Observemos que todo en text cumple los critwrios de busqueda, por lo que nos devolvera todo

if x:
    print("SI") # Nos devuelve SI, si es una coincidencia x = re.search()
else:
    print("NO")

