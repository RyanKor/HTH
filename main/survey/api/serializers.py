from rest_framework import serializers
from survey.models import SurveyMeta, StomachacheSurvey

# 복통 답변에 대한 serializer 설정


class StomachacheSurveySerializer(serializers.ModelSerializer):

    # 답변에서 설문지 주소로 갈 수 있도록 HyperlinkedRelatedField 설정
    survey = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='surveymeta-detail')

    class Meta:
        model = StomachacheSurvey
        fields = "__all__"


# 설문지에 대한 serializer 설정(복통 답변 포함)


class SurveyMetaSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    answer = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='stomachachesurvey-detail')

    # 만약 링크가 아니라 데이터 전체를 보여주고 싶으면 밑의 코드로 대체하면 됩니다.
    # answer = StomachacheSurveySerializer(read_only=True)

    class Meta:
        model = SurveyMeta
        fields = "__all__"
