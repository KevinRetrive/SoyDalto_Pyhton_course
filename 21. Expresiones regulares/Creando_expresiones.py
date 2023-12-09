# Detectando un n° CABA y ocultandolo
import re
texto = "Hola Kevin, mi numero es: +54 11 4321-4321"

pattern=r"\+\d{1,3}\s\d{1,3}\s\d{4,}-\d{4,}"

# buscamos un+, como el + es un caracter especial, lo anulamos y buscamos anteponiendo la barra invertida
# se ocultaran todos los números con ese formato en texto

reemplazo = re.sub(pattern,"(Numero oculto)",texto)
print(reemplazo)
