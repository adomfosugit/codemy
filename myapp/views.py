from django.shortcuts import render
from .models import Bakery
from .models import Bridal_Fan
from .models import Boquet
from .models import Souvenirs
# Create your views here.
def home(request):
    my_list = Bakery.objects.all()
    return render(request,
          'events/home.html',
            {'my_list' : my_list} )
def bridal(request):
    my_bridalfan = Bridal_Fan.objects.all()
    return render(request,
                  'events/bridal fan.html',
                  {'my_bridalfan': my_bridalfan})
def boquet(request):
    my_boquet = Boquet.objects.all()
    return render(request,
                  'events/boquet.html',
                  {'my_boquet': my_boquet})
def Dowryy(request):
    my_dowry = Boquet.objects.all()
    return render(request,
                  'events/dowrywrap.html',
                  {'my_dowry': my_dowry})
def souv(request):
    my_souvernirs = Souvenirs.objects.all()
    return render(request,
                  'events/souv.html',
                  {'my_souvernirs': my_souvernirs})
