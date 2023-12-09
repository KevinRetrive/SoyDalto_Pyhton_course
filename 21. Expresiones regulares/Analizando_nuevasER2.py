import re

# Cadena en la que buscaremos patrones
text = "La fecha es 23/06/2021 y el teléfono es +1-555-555-5555"

# El patrón a buscar
pattern = r"\d{2}/\d{2}/\d{4}"

# 1ero busca dos veces un digito
# seguidos de una barra
# seguido de dos veces un n°
# seguidos de una barra
# seguidos de buscar 4 veces un digito

# El texto que reemplazará el patrón
replacement = "Fecha oculta"

# Reemplazar todas las apariciones del patrón en la cadena de texto
new_text = re.sub(pattern,replacement,text)

# Imprimiendo resultado
print(f"Texto modificado: {new_text}")


print("--------------------------------------")
# Ejemplo 2

text2 = "reemplazando todas la vocales por el asterisco"

new_text2 = re.sub("[aeiou]","*",text2)
# Busca por separado cualquiera de los caracteres entre los corchetes y reemplzar por el 2do argumento

print(new_text2)

print("--------------------------------------")
# Ejemplo 3

text3 = "kevinretrive@gmail.com"

patron = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# El + funciona como el asterisco, si halla una coincidencia le pide que devuelva esa y todas las repetidas que halle,
# sin embargo si no halla coincidencia, a diferencia del asterisco, el + no te deja seguir buscando y te devuelve un resultado inválido

# Explicación (intento)
# Con el primer + fuera del corcheta le indicamos que al menos 1 de todos esos caracteres debe presentarse antes del @, sino será inválido
# el % es como un comodin
# luego del @ buscamos lo mismo que antes del @
# luego buscamos especificamente un punto con \.
# y finalmente un dominio que tenga al menos un fin con 2 letras o más (porque no existen dominios de una letra)

result = re.match(patron,text3)
# Con match buscamos que coincida

if result:
    print("Dirección de correo válida")
else:
    print("Dirección de correo inválida")


print("--------------------------------------")
# Ejemplo 4

textoo = "Este es un ejemplo de una página web: https://www.example.com "

patroon = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# Lo que hace el ? delante de la s, es indicarle que la s no es necesaria encontrarla para que continue con la busqueda
# Esto es necesario ya que algunas URL comienzan con http sin la s al final, entonces no debe ser obligatoria

resultadoo = re.findall(patroon,textoo)

print(resultadoo)