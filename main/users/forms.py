from django_registration.forms import RegistrationForm
from users.models import CustomUser
from django import forms

# abdomen_hurted = "복부를 다친 적이 있음"
# abdomen_surgery = "복부 수술을 받은 적이 있음"
# abdomen_nothing = "해당없음"
# abdomen_history = (
#     (abdomen_hurted, "복부를 다친 적이 있음"), (abdomen_surgery,
#                                        "복부 수술을 받은 적이 있음"), (abdomen_nothing, "해당없음")
# )


class CustomUserForm(RegistrationForm):
    # abdomen_relevant = forms.MultipleChoiceField(
    #     required=True, widget=forms.CheckboxSelectMultiple, choices=abdomen_history)

    class Meta(RegistrationForm.Meta):
        model = CustomUser
        # exclude = ("id", "last_login", "is_superuser", "first_name", "last_name",
        #            "is_staff", "is_active", "date_joined", "groups", "user_permissions")
        # 분명 머가 있을텐데

        fields = ('username', 'email', 'name', 'gender', 'avatar', 'birth_date', 'height',
                  'weight', 'had_checkup', 'had_checkup_true', 'diagnosed_disease', 'taking_medicine',
                  'what_medicine', 'family_history', 'drinking', 'drinking_per_week', 'smoking',
                  'how_long_smoking', 'how_much_smoking', 'job', 'relevant_data')
                  #abdomen_relevant일단 뺌
