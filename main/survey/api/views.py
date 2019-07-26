from rest_framework import generics, mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from survey.models import SurveyMeta, StomachacheSurvey

from survey.api.permissions import IsOwnerOrNot, IsOwnerOrNot_answer
from survey.api.serializers import SurveyMetaSerializer, StomachacheSurveySerializer

from survey.models import SurveyMeta, StomachacheSurvey

from django.contrib.auth.decorators import user_passes_test

# 설문지 리스트 가져오는 class view(이름으로 검색 가능)(관리자만 가능)


class SurveyMetaListView(generics.ListAPIView):
    queryset = SurveyMeta.objects.all()
    serializer_class = SurveyMetaSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    filter_backends = [SearchFilter]
    search_fields = ["author__name"]

# 복통 답변 리스트 가져오는 class view(이름으로 검색 가능)(관리자만 가능)


class StomachacheSurveyListView(generics.ListAPIView):
    queryset = StomachacheSurvey.objects.all()
    serializer_class = StomachacheSurveySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    filter_backends = [SearchFilter]
    search_fields = ["survey__author__name"]

# 설문지 내용 보기(작성자만 가능)


class SurveyMetaViewSet(
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):

    queryset = SurveyMeta.objects.all()
    serializer_class = SurveyMetaSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrNot]

# 설문지 만들기(작성자만 가능)


class SurveyMetaCreateView(generics.CreateAPIView):
    queryset = SurveyMeta.objects.all()
    serializer_class = SurveyMetaSerializer

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)


# 복통 답변 상세사항 보고, 업데이트하는 class view(설문지를 만들때 자동으로 만들어지기 때문에 업데이트를 넣었습니다.)

class StomachacheSurveyViewSet(
        mixins.UpdateModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    queryset = StomachacheSurvey.objects.all()
    serializer_class = StomachacheSurveySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrNot_answer]
