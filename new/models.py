from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Act(models.Model):
    act_name = models.CharField(max_length=20)
    act_shname = models.CharField(max_length=5)
    description = models.TextField()

    def __str__(self):
        return f"{self.act_name}"

