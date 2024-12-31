from django.shortcuts import render
from django.http import HttpResponse

def employee(request):
    return render(request, 'employee.html')

def profile(request):
    return render(request, 'profile.html')