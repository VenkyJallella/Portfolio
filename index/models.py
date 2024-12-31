from django.db import models

class about(models.Model):
    title = models.CharField(max_length=100, blank = False)
    discription = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='about/',blank=False)

    def __str__(self):
        return self.title
    

class contactlist(models.Model):
    title = models.CharField(max_length=100, blank=False)
    discription = models.TextField(max_length=300,blank=False)
    Address = models.TextField(max_length=300, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.CharField( max_length=50, blank=False)

    def __str__(self):
        return self.email
    

class contactform(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100,blank=False)
    subject = models.CharField(max_length=100,blank=False)
    message = models.TextField(max_length=400,blank=False)

    def __str__(self):
        return self.name