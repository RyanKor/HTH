from django.urls import include, path
from profiles.api.views import ProfileListAPIView, ProfileRetrieveAPIView, ProfileUpdateAPIView


urlpatterns = [
    path("profiles/", ProfileListAPIView.as_view(), name="profile-list"),
    path("profile/<int:pk>/", ProfileRetrieveAPIView.as_view(), name="profile-detail"),
    # 24.인우 : "profile/username"으로 설정하고 싶은데 그러자면
    # ProfileRetrieveAPIView에서 lookup_url_kwargs을 설정해줘야 합니다.
    # ProfileRetrieveAPIView는 ProfileSerializer를 참조하기에 ProfileUpdateSerializer의
    # 필드값(ex:name)을 쓸 수 있긴합니다.
    path("profile/<int:pk>/update/", ProfileUpdateAPIView.as_view(), name="profile-update"),
    # 25.인우 : "profile/username"으로 설정하고 싶은데 그러자면
    # ProfileUpdateAPIView에서 lookup_url_kwargs을 설정해줘야 합니다.
    # ProfileUpdateAPIView는 ProfileUpdateSerializer을 참조하기에 ProfileUpdateSerializer의
    # 필드값만 쓸 수 있는데 문제는 ProfileUpdateSerializer의 필드값이라곤 user밖에 없다는 것입니다.
    # url까지 설정해줬으니 퍼미션을 확인해봅시다.
    # profiles/api/permissions.py로 ㄱㄱ
]