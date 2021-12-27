
from django.urls import path, include
from .views import *
from home import views

urlpatterns = [
    path('', home , name="home"),
    path('login/',views.login,name='login'),
    path('Signup',views.signup),
    path('logout/',views.signout),
   
]
