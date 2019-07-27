from rest_framework import serializers
from survey.models import SurveyMeta, StomachacheSurvey

class StomachacheSurveyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = StomachacheSurvey
        exclude = ["symptom", "created_at", "author"]


class StomachacheSurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = StomachacheSurvey
        fields = "__all__"


class SurveyMetaSerializer(serializers.ModelSerializer):

    stomach = StomachacheSurveySerializer(read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = SurveyMeta
        fields = "__all__"

