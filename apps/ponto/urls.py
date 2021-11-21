from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from apps.ponto.models.WorkBreaks import WorkBreaks
from apps.ponto.views.WorkBreaksViews import WorkBreaksViewSet

from apps.ponto.views.WorkTimeViewSet import WorkTimeViewSet

router = DefaultRouter()

router.register('work-time', WorkTimeViewSet)
router.register('work-break', WorkBreaksViewSet)

relationshipPatterns = [
    url(
        regex=r'^work-time/(?P<pk>[^/.]+)/relationships/(?P<related_field>[^/.]+)/$',
        view=WorkTimeViewSet.as_view({'get': 'retrieve_related'}),
        name='work-time-relationships'
        ),
    url(r'^work-time/(?P<pk>[^/.]+)/(?P<related_field>\w+)/$',
        WorkTimeViewSet.as_view({'get': 'retrieve_related'}),
        name='work-time-related'
        ),
]

urlpatterns = [
    url(r'ponto/', include(router.urls)),
    url(r'ponto/', include(relationshipPatterns)),

]
