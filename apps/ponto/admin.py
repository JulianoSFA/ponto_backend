from django.contrib import admin

from apps.ponto.models.WorkBreaks import WorkBreaks
from .models.WorkTime import WorkTime
#from .views.BalanceViewSet import BalanceViewSet

admin.site.register(WorkTime)
admin.site.register(WorkBreaks)
#admin.site.register(BalanceViewSet)
