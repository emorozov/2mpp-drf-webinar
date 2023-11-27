from django.urls import path
from rest_framework.routers import SimpleRouter

from profiles_api.views import HelloApiView, UserProfileViewSet


router = SimpleRouter()
router.register('users', UserProfileViewSet)

urlpatterns = [
    path('hello/', HelloApiView.as_view(), name='hello'),
] + router.urls
