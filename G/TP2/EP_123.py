# Problema 1
# El usuario ingresará un texto
# i- Calcular cuánto tardaría en decir la frase (la insertada por el usuario)
# ii- ¿cuántas palabras dijo?

# Dato
# 2 palabras == 1 segundo en promedio
# Dalton habla un 30% más veloz
 
escr=input("Ingrese un texto: ")
# print(f" El usuario dijo: {escr}")
  
# Problema 2
# Si se tarda más de 1 minuto:
# i- Decirle "para flaco, tampoco te pedi un testamento"

# Problema 3
# ¿Cuánto tardaría Dalto en decirlo?

# P1 i y ii
# Debo contar la cantidad de palabras del texto, se me ocurre transformar el texto en lista por ej.
# Luego contar los elementos y ese n° multiplicarlo por 0.5
# También se me ocurre que puedo contar el n° de espacios+1 usando el método count para cadenas, voy a probar ese
palabras=escr.count(" ")+1 # Dalto lo hizo usando un método llamado .split(), también contando los espacios, y luego la función len()
print("--------------------------------")
print(f"- El usuario dijo {palabras} palabras") # Funcionó perfecto
segundos = palabras*100//2/100
print("--------------------------------")

print(f"- Y tardó {segundos} segundos en decirlo")
print("--------------------------------")

# P2 i
if segundos > 60:
    print(" Para flaco, tampoco te pedi un testamento")
else:
    print(" Es decir, tardo menos de 1 minuto")
    # Funcionó perfecto
print("--------------------------------")

# P3
segundos_Dalto = (palabras*10//2.6/10) # En vez de dividir por 2, divido por 2.6, que es el 70% (30% más rápido)
print(f"- Pero Dalto tardaría {segundos_Dalto} segundos en decirlo")
print("--------------------------------")