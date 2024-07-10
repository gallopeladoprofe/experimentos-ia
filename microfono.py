import speech_recognition as sr

def micro():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Hablar xfi")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="es-ES")
            print(f"dijiste {text}")
            return text
        except sr.UnknownValueError:
            print("No pude entender el audio")
        except sr.RequestError as e:
            print("Error al solicitar resultados del servicio de Google Speech Recognition; {0}".format(e))