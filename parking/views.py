from django.shortcuts import render
from .models import Car, Park
from common.models import User
from aptcomplex.models import Houseinfo
from django.contrib.auth.decorators import login_required
# Create your views here.



def inquiry(request, ):
    login_session = request.session.get('login_session', '')
    owner = User.objects.get(user_id = login_session)
    inquiry_list = Car.objects.filter(owner = owner)
    context = {'inquiry_list': inquiry_list}
    return render(request, 'parking/parking-2.html', context)

#def parking_map(request):
#    if request.user.is_authenticated:
#        current_user = request.user
#        location = current_user.user_house_holder
#        building = Houseinfo.objects.get(location)
#    objects_list = Park.objects.filter(location = building_num)
#    context = {'parking_map': objects_list}
#    return render(request, 'parking/parking-1.html', context)


def parking1(request):
    return render(request, 'parking/parking-1.html')

def parking2(request):
    return render(request, 'parking/parking-1-BF2.html')

def parking3(request):
    return render(request, 'parking/parking-1-BF3.html')