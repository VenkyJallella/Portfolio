from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.aboutus,name='about'),
    path('contactus/',views.contactus,name='contact'),
]
