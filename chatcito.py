from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def hablar(oraciones):
    chatbox = ChatBot('Botcito')

    trainer = ListTrainer(chatbox)
    trainer.train([
        "Hola, ¿cómo estás?",
        "Estoy bien, gracias. ¿Y tú?",
        "Estoy bien también.",
        "Me alegra saber eso.",
        "quiero comer pollo", "prefiero el lomito árabe",
        "¿Qué necesito para construir un sistemas orientado a objetos?",
        "Primero hacer un relevamiento de datos", "Leer Yourdon"
        , "Hacer el cuadro de requerimientos", "Hola Justavo",
        "¿Conoces a la goordinadora?", "Supuestamente si"
    ])

    respuesta = chatbox.get_response(oraciones)
    #print(respuesta)
    return respuesta