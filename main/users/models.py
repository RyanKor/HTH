# 2.인우 : 프로필에 들어갈 간단한 정보를 포함해서 user모델을 커스텀했습니다.

from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar=models.ImageField(null=True, blank=True)
    # 3.인우 : 장고에서 ImageField를 쓰기 위해서는 pillow 패키지가 필수라고 합니다.
    # requirements.txt에 freeze시켜뒀습니다.
    # requriements.txt에 있는 모든 항목을 다운받으려면
    # pip install -r requirements.txt
    # 를 실행하면 됩니다.

    male="남성"
    female="여성"
    gender_choices=(
        (male, '남성'), (female, "여성")
    )
    gender=models.CharField(max_length=6, choices=gender_choices)
    # 4.인우 : 디폴트값 없으면 migration이 안 먹혀서 임의`로 넣었습니다.
    
    birth_date=models.DateField()

    height=models.PositiveSmallIntegerField(validators=[MaxValueValidator(250)])
    # 5.인우 : validator는 나중에 좀 더 손봐야 할 것 같습니다. 장난으로 키 막 300 이렇게 적을까봐 일단
    # 넣어봤어요.
    # 디폴트값 없으면 migration이 안 먹혀서 임의로 넣었습니다.

    weight=models.PositiveSmallIntegerField(validators=[MaxValueValidator(200)])
    # 6.인우 : validator는 나중에 좀 더 손봐야 할 것 같습니다. 장난으로 몸무게 막 300 이렇게 적을까봐 일단
    # 넣어봤어요.
    # 디폴트값 없으면 migration이 안 먹혀서 임의로 넣었습니다.


    name=models.CharField(max_length=10, default="")
    # 7.인우 : default값으로 이름 말고 더 좋은 의견 있으신가요?
    # 디폴트값 없으면 migration이 안 먹혀서 임의로 넣었습니다.
    # ->main/setting.py AUTH_USER_MODEL로 ㄱㄱ


    how_much_alchol = models.CharField(max_length=100, default="")
    how_much_smoke = models.CharField(max_length=100, default="")
    how_much_game = models.CharField(max_length=100, default="")

    # 위의 3개 필드는 회원가입때는 입력받지 않고 profiles에서 update할 수 있는지 확인하려고 추가했습니다.(박지환)
    # 정상적으로 실행됩니다.(박지환)
    def __str__(self):
        return self.username


    

