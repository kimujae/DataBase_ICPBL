from django.shortcuts import redirect
from .models import User

def login_required(func):
    def wrapper(request, *args, **kwargs):
        login_session = request.session.get('login_session', '')

        if login_session =='':
            return redirect('/common/login/') #로그인 링크

        return func(request, *args, **kwargs)
    return wrapper