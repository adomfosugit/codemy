from django.shortcuts import render
from .models import Bakery

# Create your views here.
def home(request):
    my_list = Bakery.objects.all()
    return render(request,
          'events/home.html',
            {'my_list' : my_list} )
