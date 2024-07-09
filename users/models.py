from django.db import models

from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    user_image = models.ImageField(upload_to='users/', null=True, blank=True)
   




class ListModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
  

class AppointmentModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    doctors = models.ForeignKey(ListModel, on_delete=models.CASCADE, related_name='appointment', null=True, blank=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    problem = models.TextField()
    

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'appointment'
        verbose_name_plural = 'appointments'





class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    
   


    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'