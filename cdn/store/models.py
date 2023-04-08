from django.db import models

# Create your models here.
class CSS(models.Model):
    description=models.TextField(max_length=500)
    css_file=models.FileField(upload_to='css/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str(self):
        return self.description

class ImageFile(models.Model):
    description=models.TextField(max_length=500)
    image_file=models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class JSFile(models.Model):
    description=models.TextField(max_length=500)
    javascript_file=models.FileField(upload_to='js/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
class PdfFile(models.Model):
    description=models.TextField(max_length=500)
    pdf_file=models.FileField(upload_to='pdf/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
