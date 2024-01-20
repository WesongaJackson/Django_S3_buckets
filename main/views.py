from django.contrib import messages
from django.shortcuts import render, redirect

from main.models import UploadImage
from .forms import UploadImageForm


# Create your views here.
def index(request):
    images = UploadImage.objects.all().order_by('-created_at')

    context = {'images': images}

    return render(request, 'index.html', context)


def upload_image(request):
    if request.method == "POST":
        form = UploadImageForm(request,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image Uploaded Successfully')
            return redirect('index')
    else:
        form = UploadImageForm()

    return render(request, 'upload_images.html', {'form': form})
