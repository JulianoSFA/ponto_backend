from rest_framework_json_api.relations import ResourceRelatedField
from rest_framework_json_api.serializers import ModelSerializer
from django.contrib.auth.models import Group

from apps.core.users.models import User


class UserSerializer(ModelSerializer):
    included_serializers = {
        'groups': 'apps.users.serializers.GroupSerializer.GroupSerializer',
    }

    group = ResourceRelatedField(
        queryset=Group.objects,
        many=False,
        related_link_view_name='group-getuserlist',
        related_link_url_kwarg='user_pk',
        self_link_view_name='user-relationships',
        required=False
    )

    class Meta:
        model = User
        fields = '__all__'
        read_only = (
            'last_login', 'is_superuser', 'is_email_verified',
            'is_active', 'created', 'updated'
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }