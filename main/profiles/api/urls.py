from django.urls import include, path
from profiles.api.views import ProfileListAPIView, ProfileRetrieveAPIView, ProfileUpdateAPIView


urlpatterns = [
    path("profiles/", ProfileListAPIView.as_view(), name="profile-list"),
    path("profile/<int:pk>/", ProfileRetrieveAPIView.as_view(), name="profile-detail"),
    # 24.인우 : "profile/username"으로 설정하고 싶은데 어떻게 하는거죠...
    path("profile/<int:pk>/update/", ProfileUpdateAPIView.as_view(), name="profile-update"),
    # 25.인우 : "profile/username"으로 설정하고 싶은데 어떻게 하는거죠...
    # url까지 설정해줬으니 퍼미션을 확인해봅시다.
    # profiles/api/permissions.py로 ㄱㄱ
]