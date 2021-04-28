from django.apps import AppConfig


class stepConfig(AppConfig):
    name = 'step'
    def ready(self):
        import step.signals