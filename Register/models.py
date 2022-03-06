from django.db import models

# Create your models here.

class Register(models.Model):
    FirstName = models.CharField(max_length=50, default='')
    LastName = models.CharField(max_length=50, default='')
    UserName = models.CharField(max_length=50, default='')
    Email = models.EmailField(max_length=50, default='')
    Country = models.CharField(max_length=50, default='')
    Mobile = models.CharField(max_length=50, default='')
    Password = models.CharField(max_length=50, default='')
    Confirm_Password = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.UserName