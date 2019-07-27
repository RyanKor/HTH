from rest_framework import serializers
from survey.models import SurveyMeta, StomachacheSurvey

# 복통 답변에 대한 serializer 설정


class StomachacheSurveyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = StomachacheSurvey
        exclude = ["symptom", "created_at", "author"]


class StomachacheSurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = StomachacheSurvey
        fields = "__all__"


# 설문지에 대한 serializer 설정(복통 답변 포함)


class SurveyMetaSerializer(serializers.ModelSerializer):
    # stomach = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name="survey-list",
    # )
    stomach = StomachacheSurveySerializer(read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    # 만약 링크가 아니라 데이터 전체를 보여주고 싶으면 밑의 코드로 대체하면 됩니다.
    # answer = StomachacheSurveySerializer(read_only=True)

    class Meta:
        model = SurveyMeta
        fields = "__all__"

# class SurveyMetaSerializer(serializers.HyperlinkedModelSerializer):
#     # author = serializers.StringRelatedField(read_only=True)

#     # 만약 링크가 아니라 데이터 전체를 보여주고 싶으면 밑의 코드로 대체하면 됩니다.
#     stomach = StomachacheSurveySerializer(read_only=True)
#     url = serializers.HyperlinkedIdentityField(
#         view_name='stomach',
#         lookup_field='stomach'
#     )

#     class Meta:
#         model = SurveyMeta
#         fields = ["url", "symptom", "author", "created_at", "stomach"]
