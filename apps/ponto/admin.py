from django.contrib import admin

from apps.ponto.models.WorkBreaks import WorkBreaks

from .models.WorkTime import WorkTime

admin.site.register(WorkTime)
admin.site.register(WorkBreaks)