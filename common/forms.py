from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm


class ProfileEditForm(UserChangeForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = get_user_model()
        fields = ["username", "email"]


class PasswordEditForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["old_password", "new_password1", "new_password2"]
