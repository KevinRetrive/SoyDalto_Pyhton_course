
frutas= ["banana", "manzana", "frutilla", "durazno", "pera", "ciruela"]

for fruta in frutas:
    if fruta == "durazno":
        continue # Le dice al bucle que esta vuelta termina ahí
    print(f"Me voy a comer una: {fruta}")

print("------------------------------------------")

for fruit in frutas:
    if fruit == "durazno":
        break 
    # Le dice al bucle que terminó porque halló durazno
    print(f"Me voy a comer una: {fruit}")
# Si deseo que se come el durazno y luego se termino, el if lo coloco después del print
# Si pusiera un else tampoco se ejecutaría si nos topamos con un break antes
    