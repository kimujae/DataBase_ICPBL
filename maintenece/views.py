from django.shortcuts import render
from .models import Maintenence
from django.views.decorators.csrf import csrf_exempt

def index_1(request):
    maintenence_list = Maintenence.objects.order_by('main_date')
    context = {'maintenence_list': maintenence_list}
    return render(request, 'myapp/index.html', context)


def detail_1(request, date):
    maintenence = Maintenence.objects.get(main_date=date)
    context = {'maintenence': maintenence}
    return render(request, 'myapp/detail_1.html', context)
