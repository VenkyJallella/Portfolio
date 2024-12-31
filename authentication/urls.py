from django.urls import path
from . import views

urlpatterns = [
    path('',views.authlogin,name='login'),
    path('registation/',views.authregistation,name='registation'),
    path('forget-password/',views.forgetpassword,name='forgetpassword'),
    path('logout/',views.authlogout, name='logout')
]
