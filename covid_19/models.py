from django.db import models

# Create your models here.
class Covid19(models.Model):
    Country=models.CharField("Country",max_length=255)
    Confirmed=models.CharField(max_length=255)
    Deaths=models.CharField(max_length=255)
    Recovered=models.CharField(max_length=255)
    Date=models.DateTimeField(auto_now_add=True) 
    
    
    def __str__(self):
        return self.Country