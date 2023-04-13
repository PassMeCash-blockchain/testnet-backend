from django.db import models

# Create your models here.
from django.db import models


class CSSFile(models.Model):
    description=models.TextField(max_length=500)
    css_file=models.FileField(upload_to='css/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=30,unique=True)
    def __str(self):
        return self.description
    def get_absolute_url(self):
        return f'cdn/assets/css/{self.slug}'

class ImageFile(models.Model):
    description=models.TextField(max_length=500)
    image_file=models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=30,unique=True)

    def __str__(self):
        return self.description
    def get_absolute_url(self):
        return f'cdn/assets/images/{self.slug}'

class JSFile(models.Model):
    description=models.TextField(max_length=500)
    javascript_file=models.FileField(upload_to='js/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=30,unique=True)
    def __str__(self):
        return self.description
    def get_absolute_url(self):
        return f'cdn/assets/js/{self.slug}'

class PdfFile(models.Model):
    description=models.TextField(max_length=500)
    pdf_file=models.FileField(upload_to='pdf/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=30,unique=True)
    def __str__(self):
        return self.description
    def get_absolute_url(self):
        return f'cdn/assets/pdf/{self.slug}'
