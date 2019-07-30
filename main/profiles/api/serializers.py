from rest_framework import serializers
from profiles.models import Profile


class ProfileDisplaySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"


stress = "스트레스를 많이 받는 편"
irregular_meals = "식사 불규칙"
greasy_meals = "기름진 음식을 많이 먹음"
irregular_sleep = "수면시간 불규칙"
nothing = "해당사항 없음"
bad_habits = (
    (stress, "스트레스를 많이 받는 편"), (irregular_meals, "식사 불규칙"),
    (greasy_meals, "기름진 음식을 많이 먹음"), (irregular_sleep, "수면시간 불규칙"),
    (nothing, "해당사항 없음")
)


class ProfileUpdateSerializer(serializers.ModelSerializer):
    relevant_data = serializers.MultipleChoiceField(bad_habits)

    class Meta:
        model = Profile
        fields = ["avatar", "gender", "birth_date", "height", "weight", "name",
                  "had_checkup", "had_checkup_true", "diagnosed_disease", "taking_medicine", 
                  "what_medicine", "family_history", "drinking", "drinking_per_week", 
                  "smoking", "how_long_smoking", "how_much_smoking", "job", "relevant_data"]


class ProfileRetrieveSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ["avatar", "gender", "birth_date", "height", "weight", "name",
                  "had_checkup", "had_checkup_true", "diagnosed_disease", "taking_medicine", 
                  "what_medicine", "family_history", "drinking", "drinking_per_week", 
                  "smoking", "how_long_smoking", "how_much_smoking", "job", "relevant_data",
                  "user"]
