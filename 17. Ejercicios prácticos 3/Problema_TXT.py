# Tenemos 2 listas, una con nombres y otra con apellidos
nombres = ["Flor", "Kevin","Farid","Agustina"]
apellidos = ["Hueche", "Retrive","Favarolo","Martinez"]

# Registrar la información en un TXT de manera óptima
with open("C:\\Users\\Kevin\\OneDrive\\Escritorio\\Pyhton\\17. Ejercicios prácticos 3\\nombres_y_apellidos.txt",'w') as archivo:
    archivo.writelines("Los datos son:\n")
    [archivo.writelines(f"\nNombre: {n}\nApellido: {a}\n -----------------------------\n") for n,a in zip(nombres,apellidos)]
    
    
# Esto que hicimos en la línea 8 es lo mismo o equivalente a escribirlo así:
#for n,a in zip(nombres,apellidos):
    #archivo.writelines(f"Nombre: {n}\n Apellido: {a}\n -----------------------------\n")
    # Pero en la línea 8 se presenta la manera de escribirlo en 1 sola línea en forma de array [] "lista"