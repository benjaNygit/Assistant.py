# Notificación de cierre

from os import path
from notifypy import Notify

# Notificación para notificar el termino del asistente.
def notify_close(name_assistent):
    notification = Notify()
    notification.title = "Asistente apagado"
    notification.message = f'{name_assistent} ya no te escucha.'
    # dirección relativa
    direccion = path.abspath(path.dirname(__file__))
    notification.icon = path.join(direccion, '../../icons/icon.png')
    notification.audio = path.join(direccion, '../../voices/apagado-asistente.wav')

    notification.send()
