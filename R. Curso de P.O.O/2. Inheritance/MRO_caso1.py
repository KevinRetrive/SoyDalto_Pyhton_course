# MRO (Method resolution order)
# Sistema en el que Python busca, prioriza y ordena métodos y atributos repetidos
# Por ej, en el caso anterior, 
# ¿Qué hubiera pasado si al usar super(), ambas clase padre hubieran tenido un método con el mismo nombre?
# Veamoslo con un ejemplo más:

class A:
    def hablar(slef):
        print("Hola desde A")

class B(A):
    def hablar(slef):
        print("Hola desde B")

class C(A):
    def hablar(slef):
        print("Hola desde C")

class D(B,C):
    def hablar(slef):
        print("Hola desde D")

d = D()  
# Esto es lo normal, es lo que esperabamos, ya que es la clase desde la cual creamos el objeto y lo llamamos
d.hablar()


