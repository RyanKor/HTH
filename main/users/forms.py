from django_registration.forms import RegistrationForm
from users.models import CustomUser

class CustomUserForm(RegistrationForm):
    # abdomen_relevant = forms.MultipleChoiceField(
    #     required=True, widget=forms.CheckboxSelectMultiple, choices=abdomen_history)

    class Meta(RegistrationForm.Meta):
        model = CustomUser
