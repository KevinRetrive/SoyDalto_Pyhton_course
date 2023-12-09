#  Creando una función que muestre la serie fibonacci
# desde el 0 y el n° dado

def fibonacci(num):
    a,b= 0,1
    fibo_lista = [0] # Para que arranquemos desde el 0
    for i in range(num):
        if b > num: return fibo_lista
        else:
            fibo_lista.append(b)
            a,b = b, a+b
    return fibo_lista

resultado= fibonacci(20)
print(resultado)

#DaltoEjerciciosResueltos para hallar si algún usuario lo resolvió mejor (más simple)
# O intentar resolverlos vos mismo más fácil.
# De todas maneras Dalto nos muestra como hacerlo en una línea
# Pero no nos lo explica, nos desafia a entender y volver a buscar que es lo que hace cada función

primos_hasta= lambda num: list(filter(lambda x: all(x % i !=0 for i in range(2, int(x**0.5)+1)), range(2,num)))
print(primos_hasta(15))