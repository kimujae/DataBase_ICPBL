from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import Houseinfo
from aptcomplex import models

class HouseInfoForm(forms.ModelForm):
    class Meta:
        model = Houseinfo
        fields = ["building_num", "house_num" , "house_holder"]
        labels = {
            "building_num": "동",
            "house_num": "호",
            "house_holder":"세대주"
        }