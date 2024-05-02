from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from ads.apps import SalesConfig
from ads.views import AdViewSet, AdsListAPIView, CommentViewSet

# TODO настройка роутов для модели

app_name = SalesConfig.name

router = SimpleRouter()
router.register('', AdViewSet, basename='ads')

comments_router = routers.NestedSimpleRouter(router, '', lookup='ad')
comments_router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [path('me/', AdsListAPIView.as_view(), name='ads'),
               path('', include(router.urls)),
               path('', include(comments_router.urls)),
               ]
