from django_filters.rest_framework import FilterSet
from rest_framework.permissions import AllowAny
from rest_framework_json_api.views import ModelViewSet, RelationshipView

from apps.ponto.models.WorkBreaks import WorkBreaks
from apps.ponto.models.WorkTime import WorkTime
from apps.ponto.serializers.WorkTimeSerializer import WorkTimeSerializer
from apps.ponto.models.TimeBlock import TimeBlock


class WorkTimeFilter(FilterSet):
    class Meta:
        model = WorkTime
        fields = {
            'id': ['in', 'exact'],
            'day': ['contains', 'icontains', 'exact'],
        }


class WorkTimeViewSet(ModelViewSet):
    serializer_class = WorkTimeSerializer
    queryset = WorkTime.objects.all()
    ordering_fields = '__all__'
    filter_class = WorkTimeFilter
    search_fields = {'id', 'day', 'last_time_block__id', 'next_time_block__id'}
    permission = [AllowAny]


class WorkTimeRelationshipView(RelationshipView):
    queryset = WorkTime.objects.all()