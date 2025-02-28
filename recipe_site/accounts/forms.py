from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(
        max_length=16,
        help_text="Обязательное поле. Не более 16 символов. Только буквы, цифры и символы @/./+/-/_."
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]