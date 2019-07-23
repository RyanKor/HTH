from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    # add_form = UserCreationForm
    # form = UserChangeForm
    model = CustomUser
    list_display = ["username", "email", "is_staff"]
    # 관리자 페이지에서 유저 모델 들어가면 유저 목록에서 뜨는 정보
    fieldsets = (
        ('Private', {'fields': ('password',)}),
        ('Profile info', {'fields': ("username", "email", "name", "gender", "birth_date",
                                     "height", "weight", "avatar")}),
        ('Anamnesis', {'fields': ('had_checkup', 'had_checkup_true',
                                  'diagnosed_disease', 'taking_medicine', 'what_medicine',
                                  'family_history')}),
        ('Social History', {
         'fields': ('drinking', 'drinking_per_week', 'smoking', 'how_long_smoking',
                    'how_much_smoking', 'job', 'relevant_data')}),
        # 'abdomen_relevant'일단 뺌
        ('Permissions', {'fields': ('is_staff',)})
    )
    # add_fieldsets = {
    #     'classes': ('wide',),
    #     'fields':('username', 'email', 'password1', 'password2')
    # }
    # add_fieldsets은 어떻게 custom하는지 모르겠음 공식문서 따라한 건데 오류 뜨네요
    # 그래서 add user할 때는 프로필 정보를 넣을 수가 없습니당...

    search_fields = ('username',)
    # 관리자 페이지에서 user검색 가능
    ordering = ('username',)
    # username대로 오름차순?정렬
    filter_horizontal = ()
    # 먼지 모름 그냥 공식문서 배낌


admin.site.register(CustomUser, CustomUserAdmin)


# # 인우 : 위의 방식으로 해도 되고 아래방식으로 해도 됩니다. 보이기는 위의 방식이 훨씬 깔끔하네요.
# admin.site.register(CustomUser)
