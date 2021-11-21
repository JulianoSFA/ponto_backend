from rest_framework import serializers
from apps.ponto.models.WorkBreaks import WorkBreaks

class WorkBreaksSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkBreaks
        fields = '__all__'