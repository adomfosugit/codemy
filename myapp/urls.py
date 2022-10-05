from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name = 'home'),
    path('bridalfan/', views.bridal, name = 'bridal_fan'),
    path('#boquet/', views.boquet, name = 'boquet'),
    path('#dowry/', views.Dowryy, name = 'dowryyy'),
    path('#souv/', views.souv, name = 'souvens'),
]