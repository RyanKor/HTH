from django.urls import include, path
# from profiles.api.views import ProfileListAPIView, ProfileRetrieveAPIView, ProfileUpdateAPIView
from profiles.api.views import ProfileListAPIView, ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"profile", ProfileViewSet)
# 이렇게 하면 프로필 조회페이지에서 업데이트도 가능함

urlpatterns = [
    path("profiles/", ProfileListAPIView.as_view(), name="profile-list"),
    path("", include(router.urls)),
    # path("profile/<int:pk>/", ProfileRetrieveAPIView.as_view(), name="profile-detail"),
    # path("profile/<int:pk>/update/", ProfileUpdateAPIView.as_view(), name="profile-update"),
]
