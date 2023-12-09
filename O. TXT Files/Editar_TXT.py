# Veremos como se editan un .txt abriendolo con otro permiso
# Lo que debemos hacer es agregar un parámetro en 2do lugar luego del lugar del archivo que es: 'w'
# Este parámetro nos da permisos de escritura
# OBS con el permiso 'w' si no encuentra el archivo te lo crea
# OBS no abre el archivo, es decir solo lo escribe, o sobre escribe
# Así:

with open("15. TXT Files\\Suscribite.txt",'w', encoding="UTF-8") as Dalto:
    
    # Sobre escribiendo el archivo con .write() o .writelines()
    #Dalto.write("Jajjaja te lo edité logi")
    
    Dalto.writelines(["Hola maestro, que tal?\n","Awantaaa\n"])
    # Para agregar más de un elemento, lo debo ingresar como un iterable, por ello los corchetes
    # Podemos observar como el .txt ya no dice lo que decía antes, sino lo que yo le pusé ahora
    Dalto.writelines(["Bien y vos?\n","Kenai\n"]) 
    # Podria hacerlo en la misma lína o así separado para seguir agregando en este lazo más texto
    
# Podríamos ir agregando información en un bucle de un for por ejemplo
print("---------------------------------------------------------------")

