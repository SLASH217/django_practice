from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"  # type: ignore[reportIncompatibleVariableOverride]
    name = "blog"
