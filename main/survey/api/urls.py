from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (SurveyMetaViewSet, SurveyMetaListView,
                    SurveyMetaCreateView)

from .views import StomachacheSurveyListView, StomachacheSurveyViewSet

router = DefaultRouter()
router.register(r"survey", SurveyMetaViewSet)
# 설문지 자세히 보기
router.register(r"answer", StomachacheSurveyViewSet)
# 답변 자세히 보고 업데이트하기

# urlpattern은 임의로 만들었는데 수정 필요합니다
urlpatterns = [
    path('surveys/', SurveyMetaListView.as_view(), name="survey-list"),
    # 설문지 리스트를 보는 url
    path('answers/', StomachacheSurveyListView.as_view(), name="answer-list"),
    # 답변 리스트를 보는 url
    path('create/survey/', SurveyMetaCreateView.as_view(), name="survey-create"),
    # 설문지를 만드는 url
    path("", include(router.urls)),
]
