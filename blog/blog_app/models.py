from django.db import models

# Create your models here.

class Posst(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=30)
    date=models.DateField()
    time=models.TimeField()
    content=models.CharField(max_length=10000)

    class Meta:
        ordering=["date","time"]

    def __str__(self):
        return self.title