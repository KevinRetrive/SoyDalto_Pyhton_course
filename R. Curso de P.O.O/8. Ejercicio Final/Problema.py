# Deseamos desarrollar un chatbot en Py que sirva de analizador de sentimientos
# La idea es que le digamos algo, y que analice cuál es el sentimiento y nos respona en base a eso

# La idea es aplicar los aspectos vistos en el video:
# API (Application Programming Interface), POO, módulos, análisis de datos... etc

# textblob es una libreria que vamos a instalar
# En el CMD ponemos py -m pip install textblob

from textblob import TextBlob # Estamos importando la clase textblob del módulo TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimientos(self,texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            # sentimient es una propiedad del objeto analisis que a su vez tiene otra propiedad que es polarity (asignaremos entre 0 y 1)
            return "Positivo"
        elif analisis.sentiment.polarity == 0:
            return "Neutral"
        else:
            return "Negativo"
        
analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimientos("Hello, im feeling bad")
print(resultado)
# No varia con lo que le pongo xq la biblioteca funciona en inglés je
# Esta es una biblioteca que utiliza el lenguaje y con IA siemple que entiende mas o menos que estamos diciendo, no tiene tanta precisión

# Para hacerlo más efectivo lo haremos con ChatGPT,
# usaremos la API de Openai para que chatGPT nos de un resultado que nos sirva
# Lo sigo en otro módulo
