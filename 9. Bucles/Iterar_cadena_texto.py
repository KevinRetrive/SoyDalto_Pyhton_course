# Recorremos texto

cadena="Hola Kevin"
numeros=[2, 4, 6, 8]

for letra in cadena:
    print(letra)
#Recorremos caracter por caracter, incluyendo espacios

num_duplicados=list()
for numero in numeros:
    num_duplicados.append(numero*2)

print(num_duplicados) # Ahora la lista tiene el doble de valor en c/elemento

# Sin embargo, podríamos hacer esto anterior con un for en una sola linea de códigos
numeros_duplicados=[x*2 for x in numeros]
print(numeros_duplicados) # Obtengo lo mismo
