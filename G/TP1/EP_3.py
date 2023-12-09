# Ejercicio 3

# Datos hasta ahora:
# De este curso se grabaron 3.5 h y tras la edición quedó en 1.5 h
# De los otros el promedio crudo fue de 5 h y tras edición quedó en 4 h
# El curso más lento de los otros fue de 7 h
# El más rápido fue de 2.5 h

# variables
cac=3.5 # curso actual crudo
cae=1.5 # curso actual editado
occp=5.0 # otros cursos crudo promedio
ocep=4.0 # otros cursos editados promedio
ocml=7.0 # otros cursos más lento
ocmr=2.5 # otros cursos más rápido


# 3) 
# i- 10 horas de este curso, ¿A cuántas de los otros equivale?
# Por lo calculado en 1) iii- nuestro curso dura 62.5% menos que el resto en promedio
rpta= 10*100 // (1-62.5/100)/100
print(f" 10 horas de nuestro curso equivalen a {rpta} horas de un curso promedio")
print("--------------------------------------")

# ii- ¿Y 10 horas de los otros a cuántas de este equivale?
# Por lo calculado nuestro curso dura 62.5% menos que el resto en promedio
rpta2= 10 * (1-62.5/100)
print(f" 10 horas de otros cursos en promedio equivalen a {rpta2} horas de un curso de SoyDalto")

