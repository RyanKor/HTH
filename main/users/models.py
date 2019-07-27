from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # 지환 : user 모델을 customize하다 보니 createsuperuser할때 default이 없는 필드의 경우 오류가 납니다.
    # 이를 방지하기 위해 createsuperuser할때도 입력할 필드들을 넣어놨지만 create_superuser 함수를 override하는편이 나을 듯합니다
    # REQUIRED_FIELDS = ['birth_date', 'email', 'height', 'weight',
    #                    'taking_medicine', 'drinking', 'how_long_smoking', 'how_much_smoking']

    def __str__(self):
        return self.username
