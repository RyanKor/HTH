from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser


# class CustomUserAdmin(UserAdmin):
#     # add_form = 
#     # form = 
#     model = CustomUser
#     list_display = ["username", "email", "is_staff", "name", "gender", "birth_date", "height", "weight", "avatar"]


# admin.site.register(CustomUser, CustomUserAdmin)


#인우 : 커스텀한 유저 모델의 필드가 확인이 안되길래 일단 위는 주석 처리하고 아래와 같이 다시 등록했어요.
admin.site.register(CustomUser)