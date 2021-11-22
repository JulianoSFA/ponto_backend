from rest_framework.serializers import ModelSerializer
from apps.ponto.models.WorkBreaks import WorkBreaks

class WorkBreaksSerializer(ModelSerializer):
    class Meta:
        model = WorkBreaks
        fields = '__all__'