# Los archivos se componen del nombre y del formato (mp4 [video e imagen]; jpg [imagen]; txt[strings "texto"])
# aprenderemos a manipular .txt es un archivo de texto plano y veremos .csv luego

# Utilizamos la función "open" y le asignamos un nombre para darle un parámetro en el código
Dalto = open("15. TXT Files\\Suscribite.txt", encoding="UTF-8") 
# Agregamos este tipo de codificación que lee todo los tipos de caracteres en cualquier sistema operativos evitando símbolos raros
#print(Dalto.read()) # Y debemos usar el método .read() para leer ese tipo de archivo

print("--------------------------------------------------------")

# ¿Y si quisiera leer sólo una línea especifica del archivo .txt?
# Uso este método para leer línea por línea:

#Lineas = Dalto.readlines()
#print(Lineas) 
# Me da un arreglo vacío, lo que ocurre es que una vez que un archivo se lee, no se puede volver a leer, hay que cerrarlo
# Entonces debemos comentar los ejemplos anteriores
# Como pueden ver el 2do elemento es \n lo cual indica un espacio en linea vacío como lo hicimos
print("--------------------------------------------------------")

# Uso este método para leer una línea específica:
Linea1 = Dalto.readline() # Si no pongo nada lee la 1er línea completa
# Dentro del paréntesis coloco un n° que le indicará el n° de caracteres que me leerá
# Es importante entender que esto puede sobrecargar a la PC si es un archivo muy grande a leer y le cargo un gran n°
# Por ello según lo que querramos hacer hay otras formas de trabajar (lo mismo para .readlines())

print(Linea1)
# Y finalmente cerrar el archivo leido se hace de la siguiente manera
Dalto.close()

# Sin embargo Pyhton se rpeocupo por este tema de tener que andar abriendo y cerrando archvios...