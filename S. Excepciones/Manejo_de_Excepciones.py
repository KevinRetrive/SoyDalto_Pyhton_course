# Cualquier suceso en un programa es un evento, desde mover el mouse, hacer click, hasta lo que sea
# En la programación podemos capturarlos para en consecuencia actuar en función de que estos ocurran
# Las excepciones también son evento que interrumpen la ejecución de otro (del código específicamente) al detectar errores

# El objetivo de este apartado es poder manejar las excepciones

"""def sumar_dos():
    a = input("ingrese el valor de a: ")
    b = input("ingrese el valor de b: ")
    resultado = int(a)+int(b)
    return resultado

print(sumar_dos())"""
# Si en vez de ingresar un n° ingreso un string en a o b, recibiré una excepción del tipo ValueError
# No puedo convertir con int a entero, algo que no sea un n°
# Por ello la manera correcta de realizar código es hacerlo y a la par testearlo

# Manejo de excepciones
# Usamos la sentencia try para intentar realizar una acción
# Seguido a esto, usamos la sentencia except para manejar el error en caso de que ocurra una excepción 
# (en ese caso, le indicamos que queremos que nos devuelva)
# Además debemos para su óptimo funcionamiento, no debemos retornar el valor, por si llegará a fallar,
# por lo que debemos realizar un bucle para que el usuario pueda volver a ingresar los datos correctamente:
def sumar_dos_mejorada():
    while True:
        a = input("ingrese el valor de a: ")
        b = input("ingrese el valor de b: ")
        try:
            resultado = int(a)+int(b)
            # break # Che mira, si esto funcionó cortala acá wacho
            # El break acá no es la mejor forma de cortar, sino que usando un else (else se puede usar tanto en el for como en el try)
        except Exception as E:
            print("Te pedi un n° salame, no ingreses otra cosa")
            print("La excepción es:", E," y su tipo es: ", type(E).__name__)
        else: # Si el except se ejecuta es porque el try lanzó una excepción, y el else NO se ejecuta, y viceversa. 
            # O sea que siempre terminamos en except o else
            break
        # Añadimos una sentencia opcional "finally", la cual se ejecuta sin importar en qué terminé el código (excepción o else)
        # Se utiliza con el fin de comunicar algo más. Rara vez es útil, es como una Fe de erratas.
        finally:
            print("Esto se ejecuta siempre wey. Código finalizado.")
    return resultado

print(sumar_dos_mejorada())

# Observación: Podríamos acceder a la excepcion si le añadimos al lado de la sentencia except el objeto de la clase Exception
# La clase Exception es la clase padre de todas las excepciones y la podemos renombrar como E y mostrarla en el código
