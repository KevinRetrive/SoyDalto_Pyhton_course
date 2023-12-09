# Ejercicio 2

# Datos hasta ahora:
# De este curso se grabaron 3.5 h y tras la edición quedó en 1.5 h
# De los otros el promedio crudo fue de 5 h y tras edición quedó en 4 h
# El curso más lento de los otros fue de 7 h
# El más rápido fue de 2.5 h

# 2) % de material que se redujo tras la edición en:
# i- el promedio de los cursos
# ii- el curso actual

# variables
cac=3.5 # curso actual crudo
cae=1.5 # curso actual editado
occp=5.0 # otros cursos crudo promedio
ocep=4.0 # otros cursos editados promedio
ocml=7.0 # otros cursos más lento
ocmr=2.5 # otros cursos más rápido

# i-
p_occp_ocep = 100 - (ocep*1000//occp)/10
print(p_occp_ocep) # El tiempo removido es del 20% en los cursos, en promedio
print("--------------------------------------")

# ii-
p_cac_cae = 100 - (cae*1000//cac)/10
print(p_cac_cae) # El tiempo removido fue del 57.2% en el curso actual
