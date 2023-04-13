from django.shortcuts import render
from .form import AssetForm
from django.shortcuts import redirect
from .models import *
from django.http import HttpResponse
from django.conf import settings
import random
import string


def generate_random_string():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# Create your views here.

def Home(request):
    return render(request, 'index.html')

def Upload (request):
    if request.method == 'POST':
        context={}
        if request.POST['fileType']=='image':
            image=ImageFile.objects.create(
                description=request.POST['description'],
                image_file=request.FILES['file']
            )
            image.slug=generate_random_string()
            context={'link':str(image.slug),'msg':'Image Upload Successfully','ref':image.get_absolute_url(),'linkref':'image'}
            image.save()
        elif request.POST['fileType']=='css':
            css=CSSFile.objects.create(
                description=request.POST['description'],
                css_file=request.FILES['file']
            )
            css.slug=generate_random_string()
            context={'link':str(css.slug),'msg':'CSS Upload Successfully','ref':css.get_absolute_url(),'linkref':'css'}
            css.save()
        elif request.POST['fileType']=='javascript':
            js=JSFile.objects.create(
                description=request.POST['description'],
                javascript_file=request.FILES['file']
            )
            js.slug=generate_random_string()
            context={'link':str(js.slug),'msg':'Javascript Upload Successfully','ref':js.get_absolute_url(),'linkref':'js'}
            js.save()

        elif request.POST['fileType']=='pdf':
            pdf=PdfFile.objects.create(
                description=request.POST['description'],
                pdf_file=request.FILES['file']
            )
            pdf.slug=generate_random_string()
            context={'link':str(pdf.slug),'msg':'PDF Upload Successfully','ref':pdf.get_absolute_url(),'linkref':'pdf'}
            pdf.save()

        return render(request,'upload.html',context)
    else:
        return render(request,'upload.html')

# def get_media_url(request, filename):
#     media_root = getattr(settings, 'MEDIA_ROOT')
#     if not media_root:
#         return HttpResponseBadRequest("MEDIA_ROOT setting is missing")
#     media_url = getattr(settings, 'MEDIA_URL')
#     if not media_url:
#         return HttpResponseBadRequest("MEDIA_URL setting is missing")
#     file_path = os.path.join(media_root, filename)
#     if not os.path.isfile(file_path):
#         return HttpResponseBadRequest("File not found")
#     return JsonResponse({"url": media_url + filename})
def GetImageAssetUrl(request,slug):
    obj=ImageFile.objects.get(slug=slug)
    media_url = getattr(settings, 'MEDIA_URL')

    return redirect(f'{media_url}{obj.image_file}')

def GetCssAssetUrl(request,slug):
    obj=CSSFile.objects.get(slug=slug)
    media_url = getattr(settings, 'MEDIA_URL')

    return redirect(f'{media_url}{obj.css_file}')
def GetJsAssetUrl(request,slug):
    obj=JSFile.objects.get(slug=slug)
    media_url = getattr(settings, 'MEDIA_URL')

    return redirect(f'{media_url}{obj.javascript_file}')

def GetPdfAssetUrl(request,slug):
    obj=PdfFile.objects.get(slug=slug)
    media_url = getattr(settings, 'MEDIA_URL')

    return redirect(f'{media_url}{obj.pdf_file}')

def GetAllImages(request):
    return HttpResponse('All Stuffs')
