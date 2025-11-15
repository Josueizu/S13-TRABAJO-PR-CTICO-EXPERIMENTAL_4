from django.conf import settings

def enviar_notificacion(msg):
    if settings.ENABLE_NOTIFICATIONS:
        print("Notificación enviada:", msg)
    else:
        print("Notificaciones desactivadas")

