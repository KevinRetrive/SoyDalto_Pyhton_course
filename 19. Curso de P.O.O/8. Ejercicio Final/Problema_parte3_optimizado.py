# Optimizando el código para cumplir los principios S.O.L.I.D.

import openai

openai.api_key = "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"

system_rol = '''Hace de cuenta que sos una analizador de sentimientos
                Yo te paso sentimientos y vos analizas el mensaje
                y me das una respuesta con al menos un caracter y como
                máximo 4 caracteres, donde -1 es negatividad máxima, 0 es neutral
                y 1 es positividad máxima (podes responder solo con ints o floats)'''

mensaje = [{"role":"system", "content": system_rol}]

# Debemos crear otra clase para poder tener una independencia de formatos
# y no cargar al código con tener que formatear y desformatear el color de nuestras letras 
# y a su vez independizar a los condicionales, porque si quisera modificarlos tendría que cambiar la clase, 
# y eso podría causar errores en otras partes del código

class Sentimiento:
    def __init__(self,nombre,color):
        self.nombre=nombre
        self.color=color
    
    def __str__(self):
        # Reemplaza los corchetes por lo que le ponemos dentro de format como argumentos en ese orden, es decir, 
        # en en primer corchete color, en el 2do nombre, si el color es 31 y nombre negativo los pone allí.
        "\x1b[1;{}m{}\x1b[0;37m".format(self.color,self.nombre)

# La clase sentimientos se responsabiliza del sentimiento en sí y su color

class AnalizadorDeSentimientos:
    def __init__(self,rangos):
        self.rangos=rangos 
        # rango va a ser una tupla con dos tuplas dentro
        # La 1er tupla contiene los rangos, 0.1 y -1 y la otra el sentimiento asociado
    
    def analizar_sentimientos(self,polaridad):
        # Lo que estoy haciendo en la línea siguiente es una forma de desempaquetar
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        # sino return muy negativo porque no estaría en el rango que ahora le vamos a dar (como el else:)
        return Sentimiento("Muy negativo","31")
    
# Mientras tanto esta ca¿lase los analiza y clasifica, independientemente del módulo llamado

rangos = [ 
          ((-0.6,-0.3),Sentimiento("Negativo","31")),
          ((-0.3,-0.1),Sentimiento("Algo negativo","31")),
          ((-0.1,0.1),Sentimiento("Neutral","33")),
          ((0.1,0.4),Sentimiento("Algo positivo","33")),
          ((0.4,0.9),Sentimiento("Positivo","32")),
          ((0.9,1),Sentimiento("Muy positivo","32"))
          ]

# print("\x1b[1;33m"+"Hola") en amarillo

analisis = AnalizadorDeSentimientos(rangos)

while True:
    user_prompt=input("\x1b[1;33m"+"\nDecime algo: "+"\x1b[0;37m")
    # Ahora creamos una lista de mensajes que chatGPT analizará
    mensaje.append({"role":"user", "content":user_prompt})
    # Con la misma lógica de lo explicado antes, sólo que ahora le indicamos a la IA 
    # que el usuario es el que ingresa el contenido y que ella lo debe analizar con el system que le asignamos
    
    # Y luego le ejecutamos el autocompletado de texto al chatGPT, de lo que interpreta del mensaje del usuario:
    completion=openai.ChatCompletion().create(
        model = "gpt-3.5-turbo",
        mesagges = mensaje,
        max_tokens = 8 
        # La cantidad de caracteres que le admito que me devuelva
        # (sin embargo, deberian no ser mayoeres a 4 porque le exigí eso)
    )
    
    # Ahora tenemos que agregar el modelo de la respuesta de la IA, que es lo que vera el usuario,
    # Y que quede registrada la charla que esta teniendo para que pueda responder en base a lo que se le solicita,
    # Es decir, que tenga memoria durante la cadena de mensajes con el usuario:
    respuesta_chatbot = completion.choices[0].message["content"]
    mensaje.append({"role":"assistant","content":respuesta_chatbot})
    
    sentimiento = analisis.analizar_sentimientos(float(respuesta_chatbot))
    # Debo convertir en float lo que nos pase porque no puede comparar con los valores de -1 a 1 el texto que le damos sino
    print(sentimiento)

