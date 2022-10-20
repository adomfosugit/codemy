from django.shortcuts import render
from .models import Bakerys

# Create your views here.
def home(request):
    my_list = Bakerys.objects.all()
    return render(request,
          'events/home.html',
            {'my_list' : my_list  } )
