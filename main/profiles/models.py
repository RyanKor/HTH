# 10.인우 : udemy강의의 방식에 따라서 profile모델을 user모델과 onetoone필드로 엮어주고, 
# 시그널로 자동생성되게 하는 방법을 택했습니다.

# from django.db import models
# from users.models import CustomUser

# class Profile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     # 11.인우 : user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # 이렇게 적고 위에 CustomUser import 지워도 같은 표현일 듯...?
#     # section7에서는 이렇게 함

#     # 12.인우 : 이렇게 OneToOneField로 연결하는 것보다 추상 모델로 연결하는게 더 나을 수도....?
#     # 그렇게 하면 admin페이지의 profile에서도 기본 정보 확인 가능할 것 같은데...
    
#     # 13.인우 : 회원가입하면서 기록하는 기본 정보는 연결된 user모델을 통해 수신->따로 필드 설정할 필요 없음.
    
#     # 14.인우 : 경과를 기록할 사진을 올릴 거라면 사진을 여러 장 올려야 하므로 아래에 Image 클래스를 만들어서 ForeingKey로 연결해줘야 함.
#     # https://tothefullest08.github.io/django/2019/06/13/Django22_image2/

#     # 15.인우 : 증상기록을 저장하는 것 역시 1:N구조이기에 ForeignKey로 엮어야 함. 
#     # '설문조사'앱의 모델에서 이 앱의 Profile모델을 ForeignKey로 연결
#     # 모델을 만들어줬으니 serializer로 가봅시다.
#     # profiles/api/serializers.py로 ㄱㄱ

#     def __str__(self):
#         return self.user.username

# 박지환 : user 모델만 이용하는 방법 시도
