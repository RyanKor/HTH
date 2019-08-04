from rest_framework import generics, mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from survey.models import SurveyMeta, StomachacheSurvey

from survey.api.permissions import IsOwnerOrNot, IsOwnerOrNot_answer
from survey.api.serializers import SurveyMetaSerializer, StomachacheSurveySerializer, StomachacheSurveyCreateSerializer

# from django.contrib.auth.decorators import user_passes_test
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

class StomachacheSurveyCreateView(generics.CreateAPIView):
    queryset = StomachacheSurvey.objects.all()
    serializer_class = StomachacheSurveyCreateSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
    # 새 인스턴스를 저장할 때 CreateModelMixin에 의해서 호출되는 함수
        author = self.request.user
        symptom = "복통"
        had_checkup = self.request.user.profile.had_checkup
        had_checkup_true = self.request.user.profile.had_checkup_true
        diagnosed_disease = self.request.user.profile.diagnosed_disease
        taking_medicine = self.request.user.profile.taking_medicine
        what_medicine = self.request.user.profile.what_medicine
        family_history = self.request.user.profile.family_history
        drinking = self.request.user.profile.drinking
        drinking_per_week = self.request.user.profile.drinking_per_week
        smoking = self.request.user.profile.smoking
        how_long_smoking = self.request.user.profile.how_long_smoking
        how_much_smoking = self.request.user.profile.how_much_smoking
        job = self.request.user.profile.job
        relevant_data = self.request.user.profile.relevant_data
        serializer.save(symptom=symptom, author=author, had_checkup=had_checkup, had_checkup_true=had_checkup_true, 
                        diagnosed_disease=diagnosed_disease, taking_medicine=taking_medicine, what_medicine=what_medicine, 
                        family_history=family_history, drinking=drinking, drinking_per_week=drinking_per_week,
                        smoking=smoking, how_long_smoking=how_long_smoking, how_much_smoking=how_much_smoking, job=job, 
                        relevant_data=relevant_data)

class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

class StomachacheSurveyRetrieveView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = StomachacheSurvey.objects.all()
    serializer_class = StomachacheSurveySerializer
    permission_classes = [IsOwnerOrNot]
    lookup_fields = ["author","id"]

class OwnSurveyListView(generics.ListAPIView):
    serializer_class = SurveyMetaSerializer
    permission_classes = [IsOwnerOrNot]
    filter_backends = [SearchFilter]
    lookup_field="author"
    search_fields = ["author__username", "symptom", "created_at"]
    def get_queryset(self):

        queryset = StomachacheSurvey.objects.filter(author=self.request.user)
        return queryset

class SurveyMetaListView(generics.ListAPIView):
    queryset = SurveyMeta.objects.all()
    serializer_class = SurveyMetaSerializer
    permission_classes = [IsAdminUser]

    filter_backends = [SearchFilter]
    search_fields = ["author__username"]





