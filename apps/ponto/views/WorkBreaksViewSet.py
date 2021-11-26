from rest_framework import viewsets
from apps.ponto.serializers.WorkBreaksSerializer import WorkBreaksSerializer
from apps.ponto.models.WorkBreaks import WorkBreaks

class WorkBreaksViewSet(viewsets.ModelViewSet):
    serializer_class = WorkBreaksSerializer
    queryset = WorkBreaks.objects.all()
