from django_registration.forms import RegistrationForm
from users.models import CustomUser

class CustomUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser
        fields=('username', 'email', 'name', 'gender', 'avatar', 'birth_date', 'height', 'weight')
        # 9.인우 : 회원가입시에 기본정보를 입력받기 위해 field를 명시해줬습니다.
        # 순서를 바꾼다거나 추가한다거나 하는 건 마음대로 해도 될 것 같습니다.
        # 다만, email을 빼면 migration이 안 되고, 
        # password를 넣으면 비밀번호 확인까지 도합해서 비밀번호를 3번이나 입력하는 기현상이 발생합니다;;
        
        # 이제 user모델에서 손 볼 건 없으니 
        # python manage.py startapp profiles로 profiles앱을 만들어 줍시다.
        # 대부분의 DRF절차가 모델 -> 직렬화 -> 뷰 -> url이므로 우리도 모델부터 설정해줍시다
        # profiles/models.py로 ㄱㄱ

