# Creando mi propia excepción personalizada
class  MiExcepcion(Exception): # Heredamos de la clase padre Exception
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguiente error:  {err}")

# Literalmente con esto tenemos una clase que crea la excepción que querramos
# Todavía no hemos creado ninguna, pero con la sentencia raise le indicamos al programa que ejecute esa excepción
# Por el simple hecho de poner raise, el código nos devuelve el error indicado. Ej:
#raise ValueError
#raise ZeroDivisionError("Que boludo, dividiste por cero")

# Lanzando mi propia excepción:
#raise MiExcepcion("Jjaajajja, persona poca culta, te falta código papá")
# Manejandola:

try:
    raise MiExcepcion("Jjaajajja, persona poca culta, te falta código papá")
except:
    print("Cómo vas a cometer ese error")
