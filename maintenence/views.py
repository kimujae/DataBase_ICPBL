from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Maintenence
from common.models import User
import datetime
from django.views.decorators.csrf import csrf_exempt
from common.decorators import login_required

@login_required
def index_1(request):
    login_session = request.session.get('login_session', '')
    user = User.objects.get(user_id=login_session)

    house = user.user_house_holder

    today = datetime.date.today()
    date = str(today.year) + str(today.month)

    maintenence = Maintenence.objects.get(House =house, main_date = date)


    context = {'maintenence': maintenence,'user':user}
    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True
    return render(request, 'Maintenence/maintenance-fee-1.html', context)



@login_required
def detail_1(request):
    login_session = request.session.get('login_session', '')
    user = User.objects.get(user_id=login_session)

    house = user.user_house_holder
    maintenence_list = Maintenence.objects.filter(House =house)[:2]
    context = {'maintenence_list': maintenence_list, 'user':user}
    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True
    return render(request, 'Maintenence/maintenance-fee-2.html', context)
