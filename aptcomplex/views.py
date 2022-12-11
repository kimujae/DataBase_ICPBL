from django.shortcuts import render
from common.models import User
# Create your views here.
def index(request) :
    context={}

    login_session = request.session.get('login_session','')

    if login_session =='':
        context['login_session']= False
    else :
        context['login_session']=True
        user = User.objects.get(user_id=login_session)
        context['user']= user


    return render(request, 'main/index.html', context)