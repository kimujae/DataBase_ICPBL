from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import User,UserProfile
from aptcomplex.models import Houseinfo
from argon2 import PasswordHasher,exceptions

class ProfileEditForm(forms.Form):

    nickname = forms.CharField(max_length=128, label = '닉네임', required=False)
    email = forms.EmailField(max_length=128 ,label="이메일", required=False)
    phone_num = forms.CharField(max_length= 128, label='전화번호', required=False)
    car_num = forms.CharField(max_length= 128, label='차량번호', required=False)


    field_order = [
        "nickname",
        "email",
        "phone_num",
        "car_num"
    ]

    def clean(self):
        cleaned_data= super().clean()

        self.nickname = cleaned_data.get('nickname','')
        self.email = cleaned_data.get('email','')
        self.phone_num = cleaned_data.get('phone_num','')
        self.car_num = cleaned_data.get('car_num','')



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





class SelecthouseinfoForm(forms.Form):
    BUILDING_NUM_CHOICES = (
        (101, '101동'),
        (102, '102동'),
        (103, '103동'),
        (104, '104동'),
        (105, '105동'),
        (106, '106동'),
        (107, '107동'),
    )
    HOUSE_NUM_CHOICES = (
        (101, '101호'), (102, '102호'), (103, '103호'), (104, '104호'), (105, '105호'), (106, '106호'), (107, '107호'),
        (201, '201호'), (202, '202호'), (203, '203호'), (204, '204호'), (205, '205호'), (206, '206호'), (207, '207호'),
        (301, '301호'), (302, '302호'), (303, '303호'), (304, '304호'), (305, '305호'), (306, '306호'), (307, '307호'),
        (401, '401호'), (402, '402호'), (403, '403호'), (404, '404호'), (405, '405호'), (406, '406호'), (407, '407호'),
        (501, '501호'), (502, '502호'), (503, '503호'), (504, '504호'), (505, '505호'), (506, '506호'), (507, '507호'),
        (601, '601호'), (602, '602호'), (603, '603호'), (604, '604호'), (605, '605호'), (606, '606호'), (607, '607호'),
        (701, '701호'), (702, '702호'), (703, '703호'), (704, '704호'), (705, '705호'), (706, '706호'), (707, '707호'),
        (801, '801호'), (802, '802호'), (803, '803호'), (804, '804호'), (805, '805호'), (806, '806호'), (807, '807호'),
        (901, '901호'), (902, '902호'), (903, '903호'), (904, '904호'), (905, '905호'), (906, '906호'), (907, '907호'),
        (1001, '1001호'), (1002, '1002호'), (1003, '1003호'), (1004, '1004호'), (1005, '1005호'), (1006, '1006호'),
        (1007, '1007호'),
        (1101, '1101호'), (1102, '1102호'), (1103, '1103호'), (1104, '1104호'), (1105, '1105호'), (1106, '1106호'),
        (1107, '1107호'),
        (1201, '1201호'), (1202, '1202호'), (1203, '1203호'), (1204, '1204호'), (1205, '1205호'), (1206, '1206호'),
        (1207, '1207호'),
        (1301, '1301호'), (1302, '1302호'), (1303, '1303호'), (1304, '1304호'), (1305, '1305호'), (1306, '1306호'),
        (1307, '1307호'),
        (1401, '1401호'), (1402, '1402호'), (1403, '1403호'), (1404, '1404호'), (1405, '1405호'), (1406, '1406호'),
        (1407, '1407호'),
        (1501, '1501호'), (1502, '1502호'), (1503, '1503호'), (1504, '1504호'), (1505, '1505호'), (1506, '1506호'),
        (1507, '1507호'),
    )

    user_building_num = forms.ChoiceField(
        label= '동정보',
        required=True,
        choices= BUILDING_NUM_CHOICES
    )


    user_house_num = forms.ChoiceField(
        label='동정보',
        required=True,
        choices= HOUSE_NUM_CHOICES
    )


    user_house_holder = forms.CharField(
        max_length=32,
        label='세대주',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'user-house-holder',
                'placeholder': '세대주'
            }
        ),
        error_messages={'required': '세대주를 입력하세요.'}
    )

    field_order = [
        'user_building_num',
        'user_house_num',
        'user_house_holder'
    ]


    def clean(self):
        cleaned_data= super().clean()

        user_building_num = cleaned_data.get('user_building_num','')
        user_house_num = cleaned_data.get('user_house_num','')
        user_house_holder = cleaned_data.get('user_house_holder', '')

        if user_building_num =='':
            return self.add_error('user_building_num','동정보를 선택해주세요')
        elif user_house_num =='':
            return self.add_error('user_house_num','호 정보를 선택해주세요.')
        else :
            try:
                houseinfo = Houseinfo.objects.filter(building_num = user_building_num , house_num = user_house_num)
            except Houseinfo.DoesNotExist:
                return self.add_error('user_building_num','가입 불가능한 사용자입니다. 관리실로 문의주세요.')


            try :
                houseinfo = Houseinfo.objects.filter(building_num = user_building_num , house_num =user_house_num, house_holder = user_house_holder)
            except Houseinfo.DoesNotExist:
                return self.add_error('user_house_holder','세대주가 다릅니다.')

            self.user_building_num = user_building_num
            self.user_house_num = user_house_num
            self.user_house_holder = user_house_holder





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
            'user_last_name'
            #'user_building_num',
            #'user_house_num'
        ]


    def clean(self):
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id','')
        user_pwd = cleaned_data.get('user_pwd','')
        user_first_name = cleaned_data.get('user_first_name','')
        user_last_name = cleaned_data.get('user_last_name','')
        #user_building_num = cleaned_data.get('user_building_num', '')
        #user_house_num = cleaned_data.get('user_house_num','')

        if not 4 <= len(user_id) <= 16 :
            return self.add_error('user_id', '아이디는 4~16자로 입력해주세요.')
        elif 8 > len(user_pwd):
            return self.add_error('user_pwd', '비밀번호는 8자 이상으로 설정해주세요.')
        else :
            self.user_id = user_id
            self.user_pwd = PasswordHasher().hash(user_pwd)
            self.user_first_name = user_first_name
            self.user_last_name = user_last_name
            #self.user_building_num = user_building_num
            #self.user_house_num = user_house_num