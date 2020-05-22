from django.urls import path, include

from rest_framework.routers import DefaultRouter

from user_profile.views import UserProfileViewSet, LoginViewSet, UserProfileFeedViewSet

router = DefaultRouter()
router.register('profile', UserProfileViewSet)
router.register('login', LoginViewSet, basename='login')
router.register('feed', UserProfileFeedViewSet)

urlpatterns = [
    path('', include(router.urls))
]