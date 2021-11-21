from rest_framework import viewsets
from apps.ponto.serializers.WorkBreaksSerializer import WorkBreaksSerializer

class WorkBreaksViewSet(viewsets.ModelViewSet):
    serializer_class = WorkBreaksSerializer
    queryset = WorkBreaksSerializer.objects.all()
