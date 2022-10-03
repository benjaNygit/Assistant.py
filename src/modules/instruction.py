# Instrucciones

# retorna texto a partir de la palabra clave.
# si no se uso la keyword retorna None
def instruction(keyword, audio):
    if keyword in audio:
        audio = audio.replace(keyword, ' ').strip()
        return audio
    return None
