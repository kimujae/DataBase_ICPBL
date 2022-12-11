from django.shortcuts import HttpResponse, redirect, render
from django.views.decorators.csrf import csrf_exempt

from common.models import User
from .forms import SeatForm
from common.decorators import login_required
# Create your views here.
def index(request):

    return render(request, 'reservation/reservation.html', {})


@login_required
def reservation(request):
    login_session = request.session.get('login_session', '')
    user = User.objects.get(user_id=login_session)

    context= {}

    if login_session =='':
        context['login_session']= False
    else :
        context['login_session']=True

    context['complaint'] = False
    context['user'] =user

    if request.method == "POST":

        seat = request.POST['seat']
        context['seat'] = seat
        print(seat)
        return render(request, 'reservation/reserve-swim-complete.html',context)
    else:
        return render(request, 'reservation/reserve-swim.html', context)


@login_required
def complete(request):
    login_session = request.session.get('login_session', '')
    user = User.objects.get(user_id=login_session)

    context = {}

    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True

    context['complaint'] = False
    context['user'] = user

    return render(request, 'reservation/reserve-swim-complete.html', context)



@login_required
def hreservation(request):
    login_session = request.session.get('login_session', '')
    user = User.objects.get(user_id=login_session)

    context = {}

    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True

    context['complaint'] = False
    context['user'] = user

    if request.method == "POST":
        seat = request.POST['seat']
        print(seat)
        return render(request, 'reservation/reserve-health-complete.html', context)


    else:
        return render(request, 'reservation/reserve-health.html', context)

@login_required
def hcomplete(request):

    return render(request, 'reservation/reserve-health-complete.html')

@login_required
def sreservation(request):
    if request.method == "POST":
        return redirect("reservation:scomplete")

    else:
        return render(request, 'reservation/reserve-study.html')

@login_required
def scomplete(request):

    return render(request, 'reservation/reserve-study-complete.html')