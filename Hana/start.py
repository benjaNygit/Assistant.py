# Asistente Hana
# Nombre inspirado en personaje de anime.

from src.modules.listen import listener
from src.notifys.notify_start import notify_start
from src.notifys.notify_close import notify_close

def run_Hana():
    notify_start('Hana')
    audio = listener()
    print(audio)
    notify_close('Hana')
