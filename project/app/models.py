from django.db import models

# Create your models here.
class Students(models.Model):
    username = models.CharField(max_length=50)
    age = models.IntegerField()
    volume=models.IntegerField()
    email = models.CharField(max_length=200)
    detail=models.CharField(max_length=200)
    phone=models.IntegerField()
    subscribe=models.CharField(max_length=200)
    dob=models.DateField()
    gender=models.CharField(max_length=50)
    resume=models.FileField()
    profile_pic=models.FileField()



