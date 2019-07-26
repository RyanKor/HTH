from users.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Profile

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # 27.인우 : CustomUser인스턴스가 저장이 되면 해당 인스턴스를 OneToOne필드의 값으로 하는
        # 프로필 모델을 만들라는 시그널입니다.
        # 시그널을 만들어줬으니 profiles/apps.py로 가줍시다.
