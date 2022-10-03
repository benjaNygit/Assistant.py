# Escuchar

import speech_recognition as sr

# audio desde el microfono, retorna str
def listener():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print('Te escucho.')
        recognize.adjust_for_ambient_noise(source)
        pc = recognize.listen(source)
        audio = recognize.recognize_google(pc, language='es')
    return audio

