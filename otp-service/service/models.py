from django.db import models

# Create your models here.
class phoneModel(models.Model):
    Mobile = models.IntegerField(blank=False)
    counter = models.IntegerField(default=0, blank=False)
    wait_time=models.DateTimeField(blank=True,null=True)
    
    def __str__(self):
        return str(self.Mobile)
