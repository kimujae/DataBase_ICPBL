from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import User
from argon2 import PasswordHasher,exceptions
from aptcomplex import models

class ProfileEditForm(UserChangeForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = get_user_model()
        fields = ["username", "email"]


class PasswordEditForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["old_password", "new_password1", "new_password2"]




class LoginForm(forms.Form):
    user_id = forms.CharField(
        max_length=32,
        label='아이디',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'user-id',
                'placeholder': '아이디'
            }
        ),
        error_messages={'required': '아이디를 입력해주세요.'}
    )


    user_pwd = forms.CharField(
        max_length= 128,
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'user-pwd',
                'placeholder': '비밀번호'
            }
        ),
        error_messages={'required': '비밀번호를 입력해주세요.'}
    )

    field_order = [
        'user_id',
        'user_pwd'
    ]

    def clean(self):
        cleaned_data= super().clean()

        user_id = cleaned_data.get('user_id','')
        user_pwd = cleaned_data.get('user_pwd','')


        if user_id =='':
            return self.add_error('user_id','아이디를 다시 입력해주세요.')
        elif user_pwd =='':
            return self.add_error('user_pwd','비밀번호를 다시 입력해주세요.')
        else :
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                return self.add_error('user_id','아이디를 다시 입력해주세요.')

            try :
                PasswordHasher().verify(user.user_pwd, user_pwd)
            except exceptions.VerifyMismatchError:
                return self.add_error('user_pwd','비밀번호가 다릅니다.')

            self.login_session = user.user_id
class RegisterForm(forms.ModelForm):
    user_id = forms.CharField(
        label = '아이디',
        required= True,
        widget= forms.TextInput(
            attrs={
                'class' : 'user-id',
                'placeholder' : '아이디'
            }
        ),
        error_messages={'required' : '아이디를 입력해주세요.'}
    )

    user_pwd = forms.CharField(
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'user-pwd',
                'placeholder': '비밀번호'
            }
        ),
        error_messages={'required': '비밀번호를 입력해주세요.'}
    )

    user_first_name = forms.CharField(
        label='성',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'user-first-name',
                'placeholder': '성'
            }
        ),
        error_messages={'required': '성을 입력해주세요.'}
    )

    user_last_name = forms.CharField(
        label='이름',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'user-last-name',
                'placeholder': '이름'
            }
        ),
        error_messages={'required': '이름을 입력해주세요.'}
    )

    class Meta:
        model = User
        fields = [
            'user_id',
            'user_pwd',
            'user_first_name',
            'user_last_name',
            'user_building_num',
            'user_house_num'
        ]


    def clean(self):
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id','')
        user_pwd = cleaned_data.get('user_pwd','')
        user_first_name = cleaned_data.get('user_first_name','')
        user_last_name = cleaned_data.get('user_last_name','')
        user_building_num = cleaned_data.get('user_building_num', '')
        user_house_num = cleaned_data.get('user_house_num','')

        if not 4 <= len(user_id) <= 16 :
            return self.add_error('user_id', '아이디는 4~16자로 입력해주세요.')
        elif 8 > len(user_pwd):
            return self.add_error('user_pwd', '비밀번호는 8자 이상으로 설정해주세요.')
        else :
            self.user_id = user_id
            self.user_pwd = PasswordHasher().hash(user_pwd)
            self.user_first_name = user_first_name
            self.user_last_name = user_last_name
            self.user_building_num = user_building_num
            self.user_house_num = user_house_num