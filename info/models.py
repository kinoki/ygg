from django.db import models
from core.models import TimeStampedModel


class Detail(TimeStampedModel):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
