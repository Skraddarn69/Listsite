from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class List(models.Model):
    listname=models.CharField(max_length=255)
    cuser=models.ForeignKey(User,on_delete=models.CASCADE)
    cdate=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.listname

class Object(models.Model):
    objectname=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=5,decimal_places=2)
    purchased=models.BooleanField(default=False)
    list=models.ForeignKey(List,on_delete=models.CASCADE)

    def __str__(self):
        return self.objectname