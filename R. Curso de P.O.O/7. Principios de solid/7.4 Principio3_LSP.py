# LSP: Liskovs´s substitution principle
# Este principio estables que si una clase B hereda de A, es decir es una sub clase
# la clase A debería poder utilizarse en todos los lugares donde  B puede utilizarse
# Ej:

# class Ave:
#     def volar(self):
#         return "Estoy volando"
    
# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"

# SI creamos un objeto Ave que vuele podríamos tener problemas si la instanciamos luego en la sub clase pinguinos
# Creamos una función para hacer volar

# def hacer_volar(ave = Ave): 
#     return ave.volar()
#Le estamos indicando que el parámetro que le insertemos va a ser de la clase Ave
# CTRL + K + C para comentar varias líneas

#print(hacer_volar(Pinguino()))
# Nos dice que no puede volar, qué pasa?? La cuestión es que todo lo que la clase A puede hacer, la subclase B no puede
# Y eso es incorrecto, porque conceptualmente no respeta lo que sería herencia, es decir, en la vida real es así, un pinguino es un ave
# Pero en programación no es tan simple, debemos respetar el 3er principio, por ello es que la forma correcta de hacer esto es:

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"
    
class AveNoVoladora(Ave):
    pass

# Esta es la manera correcta de ejecutar lo que queríamos hacer, ya que en Ave podemos insertar todas las caracteristicas en común de las ave
# Y en las otras dos sub-clases clasificarlas por voladoras y no voladoras recategorizando, y en ambas se heredan las caracteristicas de Ave
