
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from common.forms import ProfileEditForm, PasswordEditForm
from aptcomplex.forms import HouseInfoForm
from .forms import RegisterForm, LoginForm, SelecthouseinfoForm
from .models import User,UserProfile
from aptcomplex.models import Houseinfo




def drop(request):
    return render(request, 'common/mypage-drop.html')

def notice(request):

    return render(request, 'common/mypage-notice.html')

def register(request):
    #houseinfo_form = HouseInfoForm()
    register_form = RegisterForm()
    select_form = SelecthouseinfoForm()

    #houseinfolist = Houseinfo.objects.all()

    context = {'form': register_form,'selectform': select_form}


    if request.method == 'GET':
        return render(request, 'common/auth-register-basic.html', context)

    elif request.method == 'POST':
        register_form = RegisterForm(request.POST)
        select_form = SelecthouseinfoForm(request.POST)
        #house_holder = request.POST.get('inputConfirmholder','')
        if select_form.is_valid():
            house_holder = Houseinfo.objects.get(building_num = select_form.user_building_num, house_num = select_form.user_house_num, house_holder = select_form.user_house_holder)
            if register_form.is_valid():
                user = User(
                    user_id = register_form.user_id,
                    user_pwd = register_form.user_pwd,
                    user_first_name = register_form.user_first_name,
                    user_last_name = register_form.user_last_name,
                    #user_building_num = register_form.user_building_num,
                    #user_house_num = register_form.user_house_num,
                    user_house_holder = house_holder
                )
                user.save()
                return redirect('/')

            else :
                context['form'] = register_form
                context['selectform'] = select_form
            return render(request, 'common/auth-register-basic.html', context)
        else:
            return render(request, 'common/auth-register-basic.html', context)

    return redirect('/')






def login(request):
    loginform= LoginForm()
    context = {'form' : loginform}

    if request.method == 'GET':
        return render(request, 'common/auth-login-basic.html', context)

    elif request.method =='POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            request.session['login_session']=loginform.login_session
            request.session.set_expiry(0)
            return redirect('/')
        else :
            context['form'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request,'common/auth-login-basic.html', context )


def logout(request):
    request.session.flush()
    return redirect('/')



def profile_view(request):
    login_session = request.session.get('login_session','')
    context = {'login_session' : login_session}
    user = User.objects.get(user_id=login_session)

    if request.method == 'GET':
        profileform= ProfileEditForm()

        if not UserProfile.objects.filter(user=user) :
            context['form'] = profileform

        else:
            profile = UserProfile.objects.get(user=user)
            context['profile'] = profile

        context['user'] = user
        return render(request, "common/mypage-profile.html",context)


    elif request.method =='POST':
        profileform = ProfileEditForm(request.POST)

        if profileform.is_valid():
            if UserProfile.objects.filter(user=user):
                profile = UserProfile.objects.get(user=user)
                context['profile'] = profile
                if not profile.nickname :
                    profile.nickname = profileform.nickname
                if not profile.email :
                    profile.email = profileform.email
                if not profile.phone_num:
                    profile.phone_num = profileform.phone_num
                if not profile.car_num:
                    profile.car_num = profileform.car_num


            else:
                profile = UserProfile(
                    nickname = profileform.nickname,
                    email = profileform.email,
                    user = user,
                    phone_num= profileform.phone_num,
                    car_num = profileform.car_num
                )
            profile.save()
            context['profile'] = profile
        else :
            context['form'] = profileform


    context['user'] = user
    return render(request, "common/mypage-profile.html", context)













@login_required(login_url="common:login")
def profile_edit(request):
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("common:profile_view")
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, "common/profile_edit.html", {"form": form})


@login_required(login_url="common:login")
def password_edit(request):
    if request.method == "POST":
        form = PasswordEditForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("common:profile_view")
    else:
        form = PasswordEditForm(request.user)
    return render(request, "common/password_edit.html", {"form": form})



