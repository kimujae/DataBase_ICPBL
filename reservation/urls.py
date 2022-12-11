from django.urls import path
from reservation import views

app_name = 'reservation'

urlpatterns = [
    #path('/', views.index, name ="index"),
    path('reservation/', views.reservation, name = "reservation"),
    path('complete/', views.complete, name="complete" ),
    path('hreservation/', views.hreservation, name = "hreservation"),
    path('hcomplete/', views.hcomplete, name="hcomplete" ),
    path('sreservation/', views.sreservation, name = "sreservation"),
    path('scomplete/', views.scomplete, name="scomplete" ),
]
