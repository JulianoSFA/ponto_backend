from django.db import models

from apps.core.users.models import User


class TimeBlock(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    day = models.DateField(null=True, blank=True)
    next_time_block = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='last_time')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='last_time')

    class Meta:
        abstract = True
