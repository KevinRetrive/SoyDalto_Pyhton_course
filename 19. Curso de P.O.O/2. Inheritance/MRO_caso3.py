# MRO (Método de resolución de orden)
# Sistema en el que Python busca, prioriza y ordena métodos y atributos repetidos
# Por ej, en el caso anterior, 
# ¿Qué hubiera pasado si al usar super(), ambas clase padre hubieran tenido un método con el mismo nombre?
# Veamoslo con un ejemplo más:

class F:
    def hablar(slef):
        print("Hola desde F")

class A:
    def hablar(slef):
        print("Hola desde A")


class B(F):
  pass

class C(A):
    def hablar(slef):
        print("Hola desde C")

class D(B,C):
    pass

d = D()  
# Nos dice hola desde F por lo explicado en el caso 2:
# Si hubiese una F, que heredara B, iría a F antes que A que que es de donde hereda C, e incluso antes que C
# porque B > C en el MRO,
# entonces así como está escrito va por F, y recién si pusiera pass en F iría por C, y finalmente por A
# ENTONCES LA REGLA ES QUE 1ERO VEMOS TODO EL ARBOL DE B Y LUEGO EL DE C, D>B>F>C>A
# A MENOS QUE TENGAN LA MISMA CLASE PADRE (ya no estaría F), Y AHÍ SERÍA D>B>C>A
d.hablar()

# Pero para joderlos y que pensemos recién ahora nos cuenta que hay una función para ver el MRO
# Se escribe la print(clase_Última.mro)
print(D.mro) # pero no me funciona porque tiene el pass, probar después porque entendí bai

# Y finalmente si quisiera acceder al método hablar desde la clase que y quiera, debo escribir
# Clase_deseada.hablar(objeto), ej:
A.hablar(d)
