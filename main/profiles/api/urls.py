from django.urls import include, path
from profiles.api.views import ProfileListAPIView, ProfileRetrieveAPIView, ProfileUpdateAPIView

urlpatterns = [
    path("profiles/", ProfileListAPIView.as_view(), name="profile-list"),
    path("profile/<str:user>/", ProfileRetrieveAPIView.as_view(), name="profile-detail"),
    path("profile/<str:user>/update/", ProfileUpdateAPIView.as_view(), name="profile-update"),
]
