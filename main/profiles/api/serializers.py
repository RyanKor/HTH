from rest_framework import serializers
from users.models import CustomUser
from profiles.models import Profile

# 16.인우 : ProfileUpdateSerializer를 설정한 이유는 2가지입니다.
# 첫째, 프로필 업데이트를 위해서입니다.
# 프로필 모델은 user만을 OneToOne필드로 갖고있기에 프로필 모델을 프로필업데이트뷰에 적용하면
# 기본정보를 수정하는 것이 불가능합니다.
# 그렇기에 customuser모델을 상속하되 username처럼 바꿔서는 안 되는 필드는 제외한 직렬화 클래스가 필요했습니다.
# (근데 뭐가 바꿔서는 안 되는 건지는 상의를 해봐야겠네요 이대로는 email필드도 넣을 수도 있는거니까) 

# 둘째, nested relationship을 이용하기 위해서입니다. 
# 프로필 리스트 뷰도 그렇고, 프로필 retrieve 뷰도 그렇고 nested relationship없이 그냥 프로필 직렬화 클래스를
# 적용해버리면 달랑 user인스턴스만 뜨는 불상사가 생기더라구요.
# nested relationship관해서는 아래 링크 타고 가시면 이해가 더 잘 될 것 같습니다.
# https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
# (nested relationship을 writable하게 바꿀 수 있다는데 이 부분은 공부가 부족해서 아직...)

# 아무튼 nested relationship을 써야 프로필 리스트 뷰에서도, 프로필 retrieve 뷰에서도 프로필 기본 정보를
# 확인할 수 있다는 것입니다.
# (이에 대한 대안으로 hyperlinkrelated필드 등이 있을 수 있겠으나 drf에 대한 이해가 부족해서 일단 
# 이렇게만 만들어놨습니다.)
class ProfileUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ["name", "gender", "birth_date", "height", "weight", "avatar"]
        # 17.인우 : 과연 이름이나 성별같은 항목을 바꿀 수 있는 값으로 둬도 좋은걸까요...?

class ProfileSerializer(serializers.ModelSerializer):  

    user = ProfileUpdateSerializer(read_only=True)
    # 18.인우 : 이렇게 설정하는 것이 nested relationship을 설정하는 방식입니다.
    # 만약 프로필 모델과 커스텀 유저 모델이 1:N관계를 이룬다면 many=true를 설정해줘야 합니다만,
    # 여기서는 OneToOneField로 엮여있기 때문에 설정하지 않았습니다.
    # 직렬화 클래스도 짰으니 profiles/api/views.py로 ㄱㄱ

    class Meta:
        model = Profile
        fields = "__all__"

