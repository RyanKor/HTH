from rest_framework import serializers
from survey.models import SurveyMeta, StomachacheSurvey

abdomen_hurted = "복부를 다친 적이 있음"
abdomen_surgery = "복부 수술을 받은 적이 있음"
abdomen_nothing = "해당없음"
abdomen_history = (
    (abdomen_hurted, "복부를 다친 적이 있음"), (abdomen_surgery,
                                       "복부 수술을 받은 적이 있음"), (abdomen_nothing, "해당없음")
)


class StomachacheSurveyCreateSerializer(serializers.ModelSerializer):
    abdomen_relevant = serializers.MultipleChoiceField(abdomen_history)

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
