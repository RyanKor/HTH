from rest_framework import permissions


class IsOwnerOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # 26.인우 : 일단 object단위 퍼미션으로 설정하긴 했는데 사실 그냥 has_permission으로 하는거나
        # 무슨 차이가 있을지 모르겠네요.
        # 이제 프로필이 자동생성되게끔 하기 위해 signals.py를 프로필 앱에 만들어줍시다.
        # profiles/signals.py로 ㄱㄱ
        return obj.user == request.user
