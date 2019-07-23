from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAdminUser
from profiles.api.permissions import IsOwnerOnly
from users.models import CustomUser
from profiles.api.serializers import ProfileSerializer


class ProfileListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]


class ProfileViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOnly]
    lookup_field = "username"


# class ProfileRetrieveAPIView(generics.RetrieveAPIView):
#     serializer_class = ProfileSerializer
#     # lookup_url_kwargs =
#     permission_classes = [IsOwnerOnly]

#     def get_object(self):
#         customuser_object = self.request.user
#         return customuser_object


# class ProfileUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = ProfileSerializer

#     permission_classes = [IsOwnerOnly]
#     # lookup_url_kwargs =

#     def get_object(self):
#         customuser_object = self.request.user
#         return customuser_object
