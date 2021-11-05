from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import ModelSerializer


class ContentTypeSerializer(ModelSerializer):
    """
    The serializer for Content Type Objects
    """

    class Meta:
        model = ContentType
        fields = ('id', 'app_label', 'model')
