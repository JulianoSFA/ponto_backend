from rest_framework import serializers
from rest_framework_json_api.relations import ResourceRelatedField

from apps.ponto.models.WorkTime import WorkTime


class WorkTimeSerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(required=True)
    end = serializers.DateTimeField(required=False)
    day = serializers.DateField(read_only=True)

    last_time_block = ResourceRelatedField(
        many=True,
        queryset=WorkTime.objects,
        required=False,
        allow_null=True,
        related_link_url_kwarg='pk',
        self_link_view_name='work-time-relationships',
        related_link_view_name='work-time-related',
    )

    next_time_block = ResourceRelatedField(
        many=True,
        queryset=WorkTime.objects,
        required=False,
        allow_null=True,
        related_link_url_kwarg='pk',
        self_link_view_name='work-time-relationships',
        related_link_view_name='work-time-related',
    )

    class Meta:
        model = WorkTime
        fields = '__all__'
