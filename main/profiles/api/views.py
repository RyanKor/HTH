from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAdminUser
from profiles.api.permissions import IsOwnerOnly
from profiles.models import Profile
from profiles.api.serializers import ProfileDisplaySerializer, ProfileRetrieveSerializer, ProfileUpdateSerializer


class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDisplaySerializer
    permission_classes = [IsAdminUser]


class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileRetrieveSerializer
    permission_classes = [IsOwnerOnly]
    lookup_field = "user"

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object


class ProfileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsOwnerOnly]
    lookup_field = "user"


    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object

# class ProfileViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsOwnerOnly]
#     lookup_field = "user"
