from django.urls import include, path
# from rest_framework.routers import DefaultRouter

# from .views import (SurveyMetaViewSet, SurveyMetaListView,
#                     SurveyMetaCreateView)

# from .views import StomachacheSurveyListView, StomachacheSurveyViewSet

# router = DefaultRouter()
# router.register(r"survey", SurveyMetaViewSet)
# # 설문지 자세히 보기
# router.register(r"answer", StomachacheSurveyViewSet)
# # 답변 자세히 보고 업데이트하기

# 인우
from .views import StomachacheSurveyCreateView
from .views import SurveyMetaListView, OwnSurveyListView, StomachacheSurveyRetrieveView

urlpatterns = [
    path('surveys/all/', SurveyMetaListView.as_view(), name="survey-list"),
    path('surveys/stomach/', StomachacheSurveyCreateView.as_view(),
         name="stomach-create"),
    path("surveys/<str:author>/", OwnSurveyListView.as_view(), name="survey-history"),
    path("surveys/<str:author>/stomach/<int:id>/",
         StomachacheSurveyRetrieveView.as_view(), name="stomach-history")
]

