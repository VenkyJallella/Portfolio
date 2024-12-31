from django.shortcuts import render
from . import models

def home(request):
    aboutdata = models.about.objects.all()
    context = {
        'about' : aboutdata
    }
    return render(request, 'index.html', context)

def aboutus(request):
    return render(request, 'about.html')

def contactus(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        

        contactformlist = models.contactform(name = name,email=email,subject=subject,message=message)
        contactformlist.save()
        
    contactlistdata = models.contactlist.objects.all()[0]
    context = {
        'contactlist' : contactlistdata
    }
    return render(request, 'contact.html',context)