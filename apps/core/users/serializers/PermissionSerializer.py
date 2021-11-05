from django.contrib.auth.models import Permission, Group
from rest_framework.serializers import ModelSerializer
from rest_framework_json_api.relations import ResourceRelatedField


class PermissionSerializer(ModelSerializer):
    """
    The serializer for Permission Objects
    """

    included_serializers = {
        'content_type': 'libs.core.users.serializers.ContentTypeSerializer.ContentTypeSerializer'
    }


    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')