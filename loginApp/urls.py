from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('logged', views.logged, name="logged"),
    path('logout', views.logout_user, name='logout'),
    path('sfdemo', views.sflogin, name='sfdemo'),
]