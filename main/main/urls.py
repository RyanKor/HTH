"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import CustomUserForm


# https://django-registration.readthedocs.io/en/3.0/activation-workflow.html

urlpatterns = [
    path('admin/', admin.site.urls),

    path("accounts/register/",
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url="/",
             ), name="django_registration_register"),
    # 1.인우 : RegistrationView가 참조할 수 있는 form은 하나입니다. 
    # 회원가입에 관련된 view이기 때문에 form에서도 당연히 user모델을 상속해야 합니다.
    # 때문에 회원가입시에 프로필에 들어갈 기본정보를 입력받고자 한다면 해당 기본정보를 
    # profile모델을 만들어 그 모델의 필드로 설정해서는 안 되고, user모델을 커스텀해야 합니다. 
    # ->user/models.py로 ㄱㄱ

    path("accounts/", include("django_registration.backends.one_step.urls")),

    path("accounts/", include("django.contrib.auth.urls")),

    # 이놈
    # api 뒤에 있는 url는 브라우저 url로 확인하기 위한 개발자용 url입니다.(박지환)
    path("api/", include("users.api.urls")),

    path("api/", include("profiles.api.urls")),

    path("api-auth/", include("rest_framework.urls")),

    path("api/rest-auth/", include("rest_auth.urls")),
        
    path("api/rest-auth/registration/", include("rest_auth.registration.urls")),

    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
]
