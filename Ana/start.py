# Asistente Hana
# Nombre inspirado en personaje de anime.

from src.modules.listen import listener
from src.modules.instruction import instruction
from src.notifys.notify_start import notify_start
from src.notifys.notify_close import notify_close

def run_Ana():
    notify_start('Ana')

    # loop principal
    while True:
        audio = listener()
        ins = instruction('Ana', audio)

        # si retorna None el loop sige.
        if ins is not None:
            break

    notify_close('Ana')
