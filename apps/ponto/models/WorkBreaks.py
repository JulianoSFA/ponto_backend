from django.db import models
from apps.core.users.models import User

class WorkBreaks(models.Model):
    KIND_OF_BREAK = (
        ("AT", "Atestado"),
        ("FR", "Feriado"),
        ("DP", "Dispensa"),
        ("FE", "Ferias"),
    )

    AFFECTED_WORKERS = (
        ("All"),
        User.objects.all(User.short_name()) #Não tenho certeza se vai listar todos a ideia seria fazer uma lista supensa
    )

    kind = models.CharField(max_lenght=3, choices=KIND_OF_BREAK, blank=False, null=False)
    name = models.CharField(max_lenght=60)
    date = models.DateField()
    affecteds_workers =  models.CharField(maxlenght=255, choices=AFFECTED_WORKERS, blank=False, null=False) 

    def __str__(self):
        return self.name


