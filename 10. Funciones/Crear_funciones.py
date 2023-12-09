# Usamos "def" para decirle al programa que crearemos una función, de la siguiente manera:
# "def NOMBRE_FUNCION():" y en la siguiente línea hacemos el código
# Y lo de adentro de los parentesis son parámetros, tal que
# Vamos a crear una función y sus parámetros (variables de la función misma)

def saludar(nombre, sexo):
    sexo = sexo.lower() # Método para que convierta todo en minúscula y así no importara como se la escriba al código, interpretará igual el sexo
    if sexo == "mujer":
        adjetivo = "mi reina"
    elif sexo == "hombre":
        adjetivo = "capo"
    else:
        adjetivo = "mi amor"
    print(f"Hola {nombre}, {adjetivo}, ¿cómo andas?")
    
saludar("Camila", "no binaria") # Pero camila no es señor... agrego otro parámetro, el sexo H o M

# Crear una función que nos retorne valores
def crear_contraseña_random(num):
    caract = "abcdefghij" # 9 caracteres
    num_entero = str(num) # Convierte en texto creo
    num=int(num_entero[0])
    # EN RESUMEN las 2 líneas anteriores lo que hago es tomo el 1er valor del parámetro que se carge en la función y lo convierto en entero
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña=f"{caract[c1]}{caract[c2]}{caract[c3]}{num*2}"
    # print(contraseña) en vez de darle print, voy a hacer que sea mia privada, no que figure en el workflow o consola
    #return contraseña # Permite poder guardar el dato, porque con print ya está una vez ejecutado, no podemos trabajar con ese dato
    # Es importante retornar los valores! Además se puede retornar más de una variables, como una tupla, por ejemplo:
    return (contraseña,num) # En realidad una tupla no requiere los parentesis, podría sacarselos


# password = crear_contraseña_random(51)
# Podría hacerlo más eficiente y devolver los valores desempaquetados, así:
password , primer_num = crear_contraseña_random(513)
frase1 = f"Tu contraseña nueva es: {password}"
frase2 = f"Tu num fue: {primer_num}"
print(frase1)
print(frase2)



