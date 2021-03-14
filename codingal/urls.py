from django.urls import path, include

from rest_framework import routers

from comments import views

router = routers.DefaultRouter()
router.register(r'comments', views.CommentViewSet)
router.register(r'replies', views.ReplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls'
    ))
]
