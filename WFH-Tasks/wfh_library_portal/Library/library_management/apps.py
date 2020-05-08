from django.apps import AppConfig


class LibraryManagementConfig(AppConfig):
    name = 'library_management'

    def ready(self):
        import library_management.signals
