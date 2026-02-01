from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, leaderboard

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = router.urls + [
    path('leaderboard/', leaderboard),
]
