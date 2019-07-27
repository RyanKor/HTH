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
        serializer.save(symptom=symptom, author=author)

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

    # def get(self, request, pk):
    #     survey = get_object_or_404(StomachacheSurvey, str=self.request.user, pk=pk)
    #     serializer = StomachacheSurveySerializer(survey)
    #     return Response(serializer.data)

# 개별 사용자가 설문 이력 목록을 볼 수 있는 view
class OwnSurveyListView(generics.ListAPIView):
    serializer_class = SurveyMetaSerializer
    permission_classes = [IsOwnerOrNot]
    filter_backends = [SearchFilter]
    lookup_field="author"
    search_fields = ["author__username", "symptom", "created_at"]
    def get_queryset(self):
    # queryset을 설정하지 않고 get_queryset함수로 대체했으므로 
    # urls.py를 보면 router등록시 basename을 설정해준 것을 볼 수 있다.
        queryset = StomachacheSurvey.objects.filter(author=self.request.user)
        return queryset

# 설문지 리스트 가져오는 class view(이름으로 검색 가능)(관리자만 가능)

class SurveyMetaListView(generics.ListAPIView):
    queryset = SurveyMeta.objects.all()
    serializer_class = SurveyMetaSerializer
    permission_classes = [IsAdminUser]
    # lookup_field="stomach"

    filter_backends = [SearchFilter]
    search_fields = ["author__username"]

# # 복통 답변 리스트 가져오는 class view(이름으로 검색 가능)(관리자만 가능)


# class StomachacheSurveyListView(generics.ListAPIView):
#     queryset = StomachacheSurvey.objects.all()
#     serializer_class = StomachacheSurveySerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]

#     filter_backends = [SearchFilter]
#     search_fields = ["survey__author__name"]

# # 설문지 내용 보기(작성자만 가능)


# class SurveyMetaViewSet(
#         mixins.RetrieveModelMixin,
#         viewsets.GenericViewSet):

#     queryset = SurveyMeta.objects.all()
#     serializer_class = SurveyMetaSerializer
#     permission_classes = [IsAuthenticated, IsOwnerOrNot]

# # 설문지 만들기(작성자만 가능)


# class SurveyMetaCreateView(generics.CreateAPIView):
#     queryset = SurveyMeta.objects.all()
#     serializer_class = SurveyMetaSerializer

#     def perform_create(self, serializer):
#         author = self.request.user
#         serializer.save(author=author)


# # 복통 답변 상세사항 보고, 업데이트하는 class view(설문지를 만들때 자동으로 만들어지기 때문에 업데이트를 넣었습니다.)

# class StomachacheSurveyViewSet(
#         mixins.UpdateModelMixin,
#         mixins.RetrieveModelMixin,
#         viewsets.GenericViewSet):
#     queryset = StomachacheSurvey.objects.all()
#     serializer_class = StomachacheSurveySerializer
#     permission_classes = [IsAuthenticated, IsOwnerOrNot_answer]
