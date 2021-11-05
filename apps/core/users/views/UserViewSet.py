from django_filters.rest_framework import FilterSet
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.core.users.models.User import User
from apps.core.users.serializers.UserSerializer import UserSerializer


class WorkTimeFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['in', 'exact'],
            'username': ['contains', 'icontains', 'exact'],
            'email': ['contains', 'icontains', 'exact'],
            'is_active': ['exact'],
        }


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    ordering_fields = '__all__'
    filter_class = WorkTimeFilter
    search_fields = {'id', 'first_name', 'middle_name', 'last_name', 'username', 'is_active'}
    permission = [AllowAny]