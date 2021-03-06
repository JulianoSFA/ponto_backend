from django.contrib.auth.models import Permission, Group
from rest_framework.serializers import ModelSerializer
from rest_framework_json_api.relations import ResourceRelatedField


class GroupSerializer(ModelSerializer):
    """
    The serializer for Group Objects
    """

    included_serializers = {
        'permissions': 'libs.core.users.serializers.PermissionSerializer.PermissionSerializer'
    }

    permissions = ResourceRelatedField(
        many=True,
        queryset=Permission.objects,
        related_link_view_name='permission-getgrouplist',
        related_link_url_kwarg='group_pk',
        self_link_view_name='group-relationships',
    )


    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')