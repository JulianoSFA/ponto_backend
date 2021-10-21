from django.db import models

class TimeBlock(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    day = models.DateField(null=True, blank=True)
    next_time_block = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='last_time')

    class Meta:
        abstract = True
