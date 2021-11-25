from django.db import models
from apps.core.users.models import User
from apps.ponto.models.TimeBlock import TimeBlock

KIND_OF_BREAK = (
        ("AT", "Atestado"),
        ("FR", "Feriado"),
        ("DP", "Dispensa"),
        ("FE", "Ferias"),
    )


class WorkBreaks(TimeBlock):

    kind = models.CharField(max_length=3, choices=KIND_OF_BREAK, blank=False, null=False)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
