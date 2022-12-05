
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from common.forms import ProfileEditForm, PasswordEditForm
from aptcomplex.forms import HouseInfoForm
from .forms import RegisterForm, LoginForm
from .models import User
from aptcomplex.models import Houseinfo



def register(request):
    houseinfo_form = HouseInfoForm()
    register_form = RegisterForm()
    houseinfolist = Houseinfo.objects.all()

    context = {'form': register_form,'houseinfoform': houseinfo_form}


    if request.method == 'GET':
        return render(request, 'common/auth-register-basic.html', context)

    elif request.method == 'POST':
        register_form = RegisterForm(request.POST)
        house_holder = request.POST.get('inputConfirmholder','')
        if register_form.is_valid():
            if not houseinfolist.filter(building_num = register_form.user_building_num, house_num=register_form.user_house_num , house_holder = house_holder):
                context['form'] = register_form
                return render(request, 'common/auth-register-basic.html', context)

            house_holder = Houseinfo.objects.get(building_num = register_form.user_building_num, house_num=register_form.user_house_num , house_holder = house_holder)
            user = User(
                user_id = register_form.user_id,
                user_pwd = register_form.user_pwd,
                user_first_name = register_form.user_first_name,
                user_last_name = register_form.user_last_name,
                user_building_num = register_form.user_building_num,
                user_house_num = register_form.user_house_num,
                user_house_holder = house_holder
            )
            user.save()
            return redirect('/')

        else :
            context['form'] = register_form
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








@login_required(login_url="common:login")
def profile_view(request):
    return render(request, "common/profile_view.html", {})


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



