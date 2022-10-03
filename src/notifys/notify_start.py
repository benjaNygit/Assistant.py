# Notificación de inicio

from os import path
from notifypy import Notify

# Notificación al iniciar el asistente.
def notify_start(name_assistent):
    notification = Notify()
    notification.title = "Asistente iniciado"
    notification.message = f'{name_assistent} te esta escuchando.'
    # dirección relativa
    direccion = path.abspath(path.dirname(__file__))
    notification.icon = path.join(direccion, '../../icons/icon.png')
    notification.audio = path.join(direccion, '../../voices/buenos-dias.wav')

    notification.send()
