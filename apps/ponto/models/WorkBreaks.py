from django.db import models
from apps.core.users.models import User

class WorkBreaks(models.Model):
    KIND_OF_BREAK = (
        ("AT", "Atestado"),
        ("FR", "Feriado"),
        ("DP", "Dispensa"),
        ("FE", "Ferias"),
    )


    kind = models.CharField(max_length=3, choices=KIND_OF_BREAK, blank=False, null=False)
    name = models.CharField(max_length=60)
    date = models.DateField()
    affecteds_workers =  models.CharField(max_length=11, default="Todos", blank=False, null=False) #gostaria de fazer em forma de lista supensa, mas nçao sei como

    def __str__(self):
        return self.name


