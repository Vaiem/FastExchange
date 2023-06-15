from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import Role
User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={ 'autocomplete': 'email'})
    )

    role = forms.ChoiceField(choices=Role.choices)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "username", "role")