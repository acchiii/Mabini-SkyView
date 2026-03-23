from django.shortcuts import render
from .models import Package


def packages(request):
    """Packages page listing all available packages."""
    all_packages = Package.objects.all()
    return render(request, 'packages/packages.html', {'packages': all_packages})
