from rest_framework import serializers
from users.models import CustomUser


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username", "email", "name", "gender", "birth_date", "height",
                  "weight", "avatar", 'how_much_alchol', 'how_much_smoke', 'how_much_game']
