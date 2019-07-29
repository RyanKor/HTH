from django.urls import include, path
from .views import StomachacheSurveyCreateView
from .views import SurveyMetaListView, OwnSurveyListView, StomachacheSurveyRetrieveView

urlpatterns = [
    path('surveys/', SurveyMetaListView.as_view(), name="survey-list"),
    path('surveys/stomach/', StomachacheSurveyCreateView.as_view(),
         name="stomach-create"),
    path("surveys/<str:author>/", OwnSurveyListView.as_view(), name="survey-history"),
    path("surveys/<str:author>/stomach/<int:id>/",
         StomachacheSurveyRetrieveView.as_view(), name="stomach-history")
]

