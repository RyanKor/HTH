from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from profiles.api.permissions import IsOwnerOnly
from users.models import CustomUser

from users.models import CustomUser
from profiles.api.serializers import ProfileUpdateSerializer, ProfileSerializer, ProfileListSerializer
# 19.인우 : 프로필 리스트 뷰가 필요한 건진 모르겠는데 일단 우리 보기 좋자고 짜봤습니다.
# 일반 사용자가 접근할 수 있으면 안 되니 IsAdminUser로 permission설정했습니다.
class ProfileListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileListSerializer
    permission_classes = [IsAdminUser]

class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'username'
    permission_classes = [IsOwnerOnly]
# 20.인우 : 사용자가 아니라면 관리자라 할지라도 사용자 프로필은 마음대로 보면 안된다고 생각해서 
# 퍼미션을 이렇게 주긴 했는데 이미 프로필리스트뷰에서 관리자가 볼 수 있게 만들었네요....
# 퍼미션 관련해서는 좀 논의를 해봐야 될 것 같습니다.

    def get_object(self):
        customuser_object = self.request.user
        return customuser_object
# 21.인우 : 프로필이야 사용자가 "자기 것만" 볼 수 있어야 하니 queryset대신에 get_object함수 설정해줬습니다

class ProfileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
# 22.인우 : 퍼미션을 프로필 retrieve뷰와 같게 설정했음에도 viewset으로 설정하지 않고 별개의 콘크리트뷰로 
# 만들 수 밖에 없는 이유입니다.
# 혼자 다른 직렬화 클래스를 참조하니까요.
# 이게 바람직한 방식인지 모르겠네요.
    permission_classes = [IsOwnerOnly]
    # lookup_url_kwargs = 

    def get_object(self):
        customuser_object = self.request.user
        return customuser_object
# 23.인우 : 갱신할 프로필도 사용자 본인 것만 해당되기 때문에 queryset대신에 get_object함수 설정해줬습니다.
# view도 만들어줬으니 profiles/api/urls.py로 ㄱㄱ
