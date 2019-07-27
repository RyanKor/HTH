from rest_framework import permissions

# 설문지를 볼때 본인인지 아닌지

class IsOwnerOrNot(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

# 답변을 볼때 본인인지 아닌지


class IsOwnerOrNot_answer(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.survey.author == request.user
