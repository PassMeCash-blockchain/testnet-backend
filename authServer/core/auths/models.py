from django.db import models
from django.contrib.auth.models import User
# Create your models here.

T = True
F = False
class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    dob = models.DateField(blank=T, null=T)
    state = models.CharField(max_length=150, blank=T, null=T)
    lga = models.CharField(max_length=150, blank=T, null=T)
    address = models.CharField(max_length=150, blank=T, null=T)
    addressAlt = models.CharField(max_length=150, blank=T, null=T)
    verified = models.BooleanField(default=F)
    created = models.DateTimeField(auto_now_add=T)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}, {self.user.email} - [{self.user.username}]"


class Stage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stageOne = models.BooleanField(default=F)
    stageTwo = models.BooleanField(default=F)
    stageThree = models.BooleanField(default=F)
    created = models.DateTimeField(auto_now_add=T)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        if self.stageOne:
            return "State one completed"
        if self.stageTwo:
            return "State one completed"
        if self.stageThree:
            return "State one completed"
        if self.stageOne and self.stageTwo and self.stageThree:
            return "completed"


class LastLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lastlogin = models.DateTimeField(auto_now_add=T)
    created = models.DateTimeField(auto_now_add=T)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.user.username} last login was {self.lastlogin}."
