from django.db import models
from django.utils import timezone
from  django.contrib.auth.models import User
# Create your models here.

class Lectures(models.Model):   

    class Status(models.TextChoices):
        WATCHED = 'W', 'Watched'
        UNWATCHED = 'UnW', 'Unwatched'
    
    class Category(models.TextChoices):
        Calculus = 'Ca', 'Calculus'
        Algebra = 'Ag', 'Algebra'
        SolidGeometery = 'Sg', "Solid Geometry"
        Dynamics = 'Dy' , 'Dynamics'


    title = models.CharField(max_length=200)
    publish = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=3, choices=Status.choices , default=Status.UNWATCHED)
    category = models.CharField(max_length=5, choices=Category.choices , default=Category.Calculus)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    lecture = models.FileField(upload_to='static/videos/' , blank=True , null=True)
    def __str__(self):
        return self.title
    

class Speakers(models.Model):
    Name = models.CharField(max_length=200)
    Job = models.CharField(max_length=200)
    photo = models.FileField(upload_to="static/images/" , blank=True , null=True)