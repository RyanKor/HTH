from rest_framework import serializers
from users.models import CustomUser


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        exclude = ("id", "last_login", "is_superuser", "first_name", "last_name",
                   "is_staff", "is_active", "date_joined", "groups", "user_permissions")
