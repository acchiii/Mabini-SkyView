from django.shortcuts import render
from .models import GalleryImage


def gallery(request):
    """Gallery page showing all uploaded images."""
    images = GalleryImage.objects.all()
    return render(request, 'gallery/gallery.html', {'images': images})
