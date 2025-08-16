from django.apps import AppConfig


class RegistroUsuariosAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registro_usuarios_app'

    def ready(self):
        from . import signals