from django.shortcuts import render
from .form import AssetForm
from .models import *

# Create your views here.

def Home(request):
    return render(request, 'index.html')

def Upload (request):
    form=AssetForm()
    if request.method == 'POST':
        print(request.FILES)
        if request.POST['fileType']=='image':
            ImageFile.objects.create(
                description=request.POST['description'],
                image_file=request.FILES['file']
            )
            # ImageFile.save()
    return render(request,'upload.html',{'form':form})
