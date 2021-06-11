from django.apps import AppConfig


class RoomConfig(AppConfig):
    name = 'conference_room'

    def ready(self):
        from . import schedular
        schedular.start()
