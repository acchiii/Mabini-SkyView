from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from gallery.models import GalleryImage
from packages.models import Package


def home(request):
    """Homepage view with featured content."""
    featured_images = GalleryImage.objects.all()[:6]
    featured_packages = Package.objects.all()[:3]
    context = {
        'featured_images': featured_images,
        'featured_packages': featured_packages,
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page view."""
    return render(request, 'core/about.html')


def contact(request):
    """Contact page with form handling."""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

        if not all([name, email, subject, message_text]):
            messages.error(request, 'Please fill in all fields.')
        else:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text,
            )
            messages.success(request, "Thank you! Your message has been sent. We'll get back to you soon.")
            return redirect('contact')

    return render(request, 'core/contact.html')