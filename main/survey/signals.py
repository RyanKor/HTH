from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SurveyMeta, StomachacheSurvey

# 설문지가 만들어지면 자동으로 복통 답변이 만들어지게
@receiver(post_save, sender=SurveyMeta)
def create_(sender, instance, created, **kwargs):
    if created:
        StomachacheSurvey.objects.create(survey=instance)
