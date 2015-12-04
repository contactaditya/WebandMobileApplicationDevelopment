from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Additional(models.Model):
    user=models.OneToOneField(User)
    phone=models.CharField(max_length=100)


