from rest_framework import serializers
from profiles.models import Profile


class ProfileDisplaySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ["avatar", "gender", "birth_date", "height", "weight", "name",
                  "diagnosed_disease", "taking_medicine", "what_medicine", "family_history",
                  "drinking", "drinking_per_week", "smoking", "how_long_smoking",
                  "how_much_smoking", "job", "relevant_data"]


class ProfileRetrieveSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ["avatar", "gender", "birth_date", "height", "weight", "name",
                  "diagnosed_disease", "taking_medicine", "what_medicine", "family_history",
                  "drinking", "drinking_per_week", "smoking", "how_long_smoking",
                  "how_much_smoking", "job", "relevant_data", "user"]
