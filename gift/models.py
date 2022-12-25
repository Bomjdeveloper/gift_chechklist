from django.db import models
from django.contrib.auth.models import User


class Gift(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    gift_name = models.CharField(max_length=100)
    person_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.gift_name