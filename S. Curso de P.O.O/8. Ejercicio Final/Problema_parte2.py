# Instalo en el CMD
# Pongo "py -m pip install openai" o "pip install openai"

import openai

# Para conseguir la api-key debemos ir a internet y googlear y entrar a openAI.com 
# nos logueamos, vamos a view keys, y generamos una nueva, y nos anotamos el código secreto
# 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

openai.api_key = "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"

# Ahora le damos las instrucciones al ChatGPT:
system_rol = '''Hace de cuenta que sos una analizador de sentimientos
                Yo te paso sentimientos y vos analizas el mensaje
                y me das una respuesta con al menos un caracter y como
                máximo 4 caracteres, donde -1 es negatividad máxima, 0 es neutral
                y 1 es positividad máxima (podes responder solo con ints o floats)'''

mensaje = [{"role":"system", "content": system_rol}]
# Tenemos 3 tipos de roles, system(rol que le dice cómo se tiene que comportar la IA) 
# user(lo que le dice el usuario, es decir quien escribe el mensaje)
# o assistant(es la respuesta que nos da la IA)
# Entonces como yo estoy definiendo su rol, lo pongo en system y le doy el contenido

class AnalizadorDeSentimientos:
    def analizar_sentimientos(self,polaridad):
        if polaridad > -0.6 and polaridad <= -0.3:
            return "\x1b[1;31m"+"Negativo"+"\x1b[0;37m"
            # Este codigo es para poder darle color al texto
            # este caso el rojo, el 32 es verde y 33 amarillo 
            # y uso este al final para volver al blanco "\x1b[0;37m"
        elif polaridad > -0.3 and polaridad <= -0.1:
            return "\x1b[1;31m"+"Algo negativo"+"\x1b[0;37m"
        elif polaridad >= -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m"+"Neutral"+"\x1b[0;37m"
        elif polaridad >= 0.1 and polaridad <= 0.4:
            return "\x1b[1;33m"+"Algo positivo"+"\x1b[0;37m"
        elif polaridad >= 0.4 and polaridad <= 0.9:
            return "\x1b[1;32m"+"Positivo"+"\x1b[0;37m"
        elif polaridad >= 0.9:
            return "\x1b[1;32m"+"Muy positivo"+"\x1b[0;37m"
        else:
            return "\x1b[1;31m"+"Muy negativo"+"\x1b[0;37m"

# print("\x1b[1;33m"+"Hola") en amarillo

analisis = AnalizadorDeSentimientos()
resultado= analisis.analizar_sentimientos(0.92)
print(resultado)

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


