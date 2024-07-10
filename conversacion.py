from chatcito import hablar
from texto_a_voz import leer

palabras = input('Hablar: ')
print("")
while(palabras):
    if palabras.strip() == 's':
        break
    if palabras.strip() is not None:
        oracion = hablar(palabras)
        print(f"respuesta: {oracion}")
        leer(oracion)
        palabras = input('Hablar: ')