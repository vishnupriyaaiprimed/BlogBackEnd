from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=500)
    author=models.CharField(max_length=30)
    date=models.DateField()
    time=models.TimeField()
    content=models.CharField(max_length=10000)

    class Meta:
        ordering=["date","time"]

    def __str__(self):
        return self.title

class Profile1(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}Proflie'
