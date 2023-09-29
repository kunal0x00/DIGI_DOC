from django.db import models

# Create your models here.
class Contact(models.Model):
    sno= models.AutoField(primary_key=True)#django automatically takes it as primarly even if i not write primary_key=true
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content= models.TextField()
    timeStamp =models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) :
        return 'Message from' + self.name + '-' + self.email
    
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)