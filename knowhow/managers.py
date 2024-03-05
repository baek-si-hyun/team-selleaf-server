from django.db import models


class KnowhowManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(knowhow_status=True)
