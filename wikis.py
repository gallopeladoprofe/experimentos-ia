import wikipedia
from texto_a_voz import leer

search = 'busca derecho romano'.strip()
wikipedia.set_lang("es")
wiki = wikipedia.summary(search, 1)

print(wiki)
leer(wiki)


