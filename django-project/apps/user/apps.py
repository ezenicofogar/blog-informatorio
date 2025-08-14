from django.apps import AppConfig
from django.db.models.signals import post_migrate


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user'

    def ready(self):
        from . import signals
        post_migrate.connect(signals.create_Ejemplo_group, sender=self)
        return super().ready()