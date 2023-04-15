from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number=models.IntegerField()
    date_of_birth=models.DateField(blank=True,null=True)

    def __str__(self):
        return self.user.username

