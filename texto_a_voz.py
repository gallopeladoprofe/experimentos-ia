import pyttsx3

def leer(texto):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    for voice in voices:
        if 'spanish' in voice.languages or 'es' in voice.id:
            engine.setProperty('voice', voice.id)
            break

    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)

    #text = "Me gustaria leer un libro de literatura inglesa"

    engine.say(texto)

    engine.runAndWait()