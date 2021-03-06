from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProducerConfig(AppConfig):
    name = "django_producer"
    verbose_name = _("Django Producer")
