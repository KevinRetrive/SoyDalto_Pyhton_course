# La manera de iterar un diccionario es:

diccionario={
    "nombre": "kevin",
    "apellido":"retrive",
    "edad": 26
}

#for key in diccionario:
#    print(key) 
# Muestra los key, las claves por defecto, no importa si pongo otra palabra en vez de key
# Pero si uso el método .items() puedo acceder a ambos key,valor en forma de tupla:

for variable in diccionario.items():
    #print(key) o mejor:
    key=variable[0]
    value=variable[1]
    print(f"La clave es: {key} y su valor es: {value}")