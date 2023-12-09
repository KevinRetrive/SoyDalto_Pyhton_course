# Utilizando el permiso 'a' agregamos el arhivo lo que le digamos
# Es decir, NO sobre escribe, sino que agrega, y las veces que lo corramos agrega
# Si corremos 3 veces agregara 3 veces:

#with open("15. TXT Files\\Suscribite.txt",'a', encoding="UTF-8") as Dalto:
   
 #   Dalto.writelines(["MM fui agregado al grupo\n","Corrida1\n"])

# Ejemplo usando un bucle para agregar varias linea

with open("15. TXT Files\\Suscribite.txt",'a', encoding="UTF-8") as Dalto:
    Dalto.write("\n")
    for i in range(5):
        Dalto.write(f"Línea {i+1} agregada\n")
        
# Nos desafía a hacer lo mismo en una sola línea de codigo usando for