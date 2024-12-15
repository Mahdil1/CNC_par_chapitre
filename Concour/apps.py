from django.apps import AppConfig


class ConcourConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Concour'

    def ready(self):
        import Concour.signals