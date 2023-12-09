# Si una primer condición no se cumple, y tenemos una intermedia usamos else if, con el condicional elif

ingreso_mes = 7000 # Dólares

if ingreso_mes > 10000:
    print("Sos re cheto")
elif ingreso_mes >6000:
    print("ahorras piola")
elif ingreso_mes > 1000:
    print("Clase media en Argentina")
else:
    print("Sos pobre")
    
# También podemos realizar condiciones anidadas, si precisamos que se cumplan dos condiciones, por ejemplo:

gasto_mes = 5000 # Dólares

if ingreso_mes > 10000:
    if ingreso_mes - gasto_mes < 0: # Diferencia entre ingreso y gastos
        print("Estas en déficit, debes guita")
    elif ingreso_mes - gasto_mes > 2000:
        print("Sos re careta")
    else:
        print("Y... hay que ver si te alcanza")
elif ingreso_mes >6000:
    print("ahorras piola")
elif ingreso_mes > 1000:
    print("Clase media en Argentina")
else:
    print("Sos pobre")
