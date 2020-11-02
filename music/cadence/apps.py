from django.apps import AppConfig


class CadenceConfig(AppConfig):
    name = 'cadence'

    def ready(self):
        import cadence.signals