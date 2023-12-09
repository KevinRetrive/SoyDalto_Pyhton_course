# Falto el profesor y los alumnos decidieron tomar la clase
# Un alumno es el profesor y otro el asistente
# A) Pedir la edad de los compañeros y ordenarla de menor a mayor
# B) El mayor es el profesor y el menor el asistente, ¿Quién es quién?

def datos(cantidad):
    compañeros=[]
    for i in range(cantidad): # Asumimos que vinieron 7 compañeros
        nombre = input("Ingrese su nombre: ")
        # Recordar que input siempre devuelve string
        edad = int(input("Ingrese su edad: ")) # Transformamos la edad como string en número
        compañero=(nombre , edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1]) # Recordar función sort() ordena según lo especificado
    # Ordeno a los compañeros por el key, que cuál es, es el 2do valor de la tupla, que es la edad
    # Una vez ordenados, sabemos que el primer elemento (0) de la lista es el asistente
    asistente = compañeros[0][0]
    # Recordar que tengo una tupla que dentro tiene otra, ya que para cada alumno tengo nombre y edad
    # De manera que con un [0] le indico que quiero el primer elemento (el primer alumno)
    # Y con el siguiente [0] que quiero su nombre, sino sería un [1] para saber su edad
    profesor = compañeros[-1][0] 
    # Recuerden con el -1 accedemos al último alumno de la lista por más que no sepamos cuantos hay
    return asistente,profesor
    
asistente,profesor = datos(5)
print(f"El asistente es: {asistente}")
print(f"El profesor es: {profesor}")

