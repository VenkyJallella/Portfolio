from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.employee),
    path('profile/',views.profile,name='profile'),
]
