# Cuando hablamos de métodos, no hablamos de funciones y son aplicadas a objetos (lista, texto, etc)

cadena1 = "Hola soy Kevin"
cadena2= "Bienvenido maquinola"

# Por ejemplo la función dir nos muestra en el workflow todos los métodos que se les pueden aplicar a el tipo de dato que tiene insertado
# Por ejemplo dir(5) nos mostrará todas las métodos aplicabes a datos tipo int, si fuese 3.4 serían las tipo float.. y así
# Y para que nos las muestre usamos siempre la función print, sino no veremos la respuesta

#print(dir(4))
#print(dir("kefmwekad"))

# Empezaremos viendo lo que podemos hacer con un texto
# Los métodos se escriben precedidos del dato o la variable a modificar
resultado= cadena1.upper() # Transforma todo el texto a mayúscula
# siempre es DATO.METODO
print(resultado)

# Otros métodos
# .lower() convierte a minúscula
# .caapitalize() convierte todo en minúscula y luego la primer letra a mayúscula
# .find("acá va lo que queremos buscar") buscamos una cadena en otra cadena RECORDAR que comienza a contar desde la posición 0, si no halla resultados devuelve -1
# .index("lo mismo que find") salvo que si no halla nada, nos tira un error
# .isnumeric() si es númerico devuelve True así este escrito como texto
# .isalpha() si es alphanumerico devuelve True (no incluye los espacios, caracteres especiales, etc)
# .count() devuelve el n° de ocurrencias de una subcadena en la cadena dada (cuantas veces halló esa coincidencia incluyendo espacios, caracteres), sino hay coincidencias es 0
# len(variable o dato) es una función no un método y devuelve la cantidad de caracteres que posee una cadena. 
# .endswith() verifica si una cadena termina con otra
# .startswith() verifica si una cadena empieza con otra
# .replace("lo que quiero sacar todas las veces que aparezca" , "lo que quiero poner") reemplaza una cadena por otra, si no halla el elemento en la cadena, no hará el reemplazo
# .split(",") separar cadenas con la cadena que le pasemos, por ejemplo en este caso, cada vez que haya una coma no separa la cadena transformada en lista ojo