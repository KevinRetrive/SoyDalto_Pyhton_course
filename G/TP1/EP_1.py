# Ejercicio 1

# Datos hasta ahora:
# De este curso se grabaron 3.5 h y tras la edición quedó en 1.5 h
# De los otros el promedio crudo fue de 5 h y tras edición quedó en 4 h
# El curso más lento de los otros fue de 7 h
# El más rápido fue de 2.5 h

# 1) Diferencia % entre este curso y:
# i- el más rápido de los otros cursos
# ii- el más lento de los otros cursos
# iii- el promedio de los otros cursos

# variables
cac=3.5 # curso actual crudo
cae=1.5 # curso actual editado
occp=5.0 # otros cursos crudo promedio
ocep=4.0 # otros cursos editados promedio
ocml=7.0 # otros cursos más lento
ocmr=2.5 # otros cursos más rápido

dp_cac_occp= 100 - (cac*1000//occp)/10
print(dp_cac_occp) # El curso nuestro crudo dura 30% menos que el promedio del resto crudo
# i-
dp_cae_ocml= 100 - (cae*1000//ocml)/10
print(dp_cae_ocml) # El curso nuestro dura 78.6% menos que el más lento
print("--------------------------------------")
# ii-
dp_cae_ocmr= 100 - (cae*1000//ocmr)/10
print(dp_cae_ocmr) # El curso nuestro dura 40% menos que el más rápido
print("--------------------------------------")
# iii-
dp_cae_ocep= 100 - (cae/ocep)*100
print(f"El curso nuestro dura {dp_cae_ocep} menos que el promedio del resto") # O puedo presentarlo así

# Recordad que si usamos la división doble redondeamos el n° al entero inferior para evitar los decimales largos
# Multiplico por 1000 y divido por 10 para tener el primer decimal después de la coma
# Multiplico por 10000 y divido por 100 para tener el segundo decimal después de la coma






