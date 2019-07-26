from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import profiles.signals
# 28.인우 : 솔직히 작동원리는 모르겠는데 이렇게 해줘야 시그널이 작동하나 봅니다.
# 잔말말고 해줍시다.
# 이 ProfilesConfig를 __init__.py에서 참조해주는 모양이니 
# profiles/__init__.py로 가줍시다.  