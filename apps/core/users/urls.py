from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url

from apps.core.users.views.UserViewSet import UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet)

relationshipPatterns = [
]

urlpatterns = [
    url(r'', include(router.urls)),
]
