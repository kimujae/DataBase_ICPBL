
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from common.forms import ProfileEditForm, PasswordEditForm


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
