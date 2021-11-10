from django.db import models

# Create your models here.

class Contact(models.Model):
    fullname = models.CharField(max_length=100,blank=True,null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    message = models.TextField()
    subject = models.CharField(max_length=100,)
    
    def __str__(self):
        return self.fullname