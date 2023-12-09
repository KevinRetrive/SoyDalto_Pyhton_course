# Forma óptima de abrir un .txt
# Con la función with open() abrimos y cerramos un archivo
# Con la función as puedo asignarle un nombre, porque por si no lo notamos de esta manera no lo igualabamos a un parámetro

with open("15. TXT Files\\Suscribite.txt", encoding="UTF-8") as Dalto:
    print(Dalto.read())
    # Esto significa que el archivo se abrió, se ejecuto este lazo y se cerró.
print("---------------------------------------------------------------")

# Lo mismo pero más simple, consumiendo menos recursos, menos errores de excepciones, etc

