from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import MovieViewSet, ActorViewSet, CommentAPIView
from rest_framework.routers import DefaultRouter
from .views import MovieActorAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)
# router.register('comments', CommentAPIView, 'comments')


schema_view = get_schema_view(
    openapi.Info(
        title='Movie application',
        default_version='v1',
        description='Swagger dock for rest API',
        contact=openapi.Contact(email='jamolov@hamil.com')
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view(), name='movie-actors'),
    path('auth/', obtain_auth_token),
    path('comments/', CommentAPIView.as_view(), name='comments'),
    path('comments/<int:id>/', CommentAPIView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui')
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('movies/', MovieAPIView.as_view()),
#     path('actors/', ActorAPIView.as_view())
# ]
