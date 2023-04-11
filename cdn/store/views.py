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
        elif request.POST['fileType']=='css':
            CSS.objects.create(
                description=request.POST['description'],
                css_file=request.FILES['file']
            )
        elif request.POST['fileType']=='javascript':
            JSFile.objects.create(
                description=request.POST['description'],
                javascript_file=request.FILES['file']
            )
        elif request.POST['fileType']=='pdf':
            pdfFile.objects.create(
                description=request.POST['description'],
                pdf_file=request.FILES['file']
            )

    return render(request,'upload.html',{'form':form})
