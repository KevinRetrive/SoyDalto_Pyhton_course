# MRO (Método de resolución de orden)
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
    pass

d = D()  
# Podemos ver que le da prioridad a B, ¿Por qué a C no?
# Y si pusieramos pass en B le daría a C, y finalmente si pongo pass en C, a A
# ¿Que definió que B sea de > prioridad que B? 
# Bueno, resulta que B esta antes que C como argumento en la clase C !
# Recién si no hallara el método en B, se va a C, y sino finalmente a A
# Si hubiese una F, que heredara de B, iría a F antes que A que que es de donde hereda C, porque B > C, ej en el caso 3
d.hablar()


