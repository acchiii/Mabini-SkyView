from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking
from packages.models import Package
import datetime


def booking(request):
    """Booking page with form handling."""
    packages = Package.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        date_str = request.POST.get('date', '').strip()
        guests_str = request.POST.get('guests', '').strip()
        package_choice = request.POST.get('package', '').strip()
        special_requests = request.POST.get('special_requests', '').strip()

        errors = []

        if not all([name, email, date_str, guests_str]):
            errors.append('Please fill in all required fields.')

        try:
            guests = int(guests_str)
            if guests < 1:
                errors.append('Number of guests must be at least 1.')
            elif guests > 100:
                errors.append('For groups over 100, please contact us directly.')
        except (ValueError, TypeError):
            errors.append('Please enter a valid number of guests.')

        try:
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            if date < datetime.date.today():
                errors.append('Please select a future date.')
        except (ValueError, TypeError):
            errors.append('Please enter a valid date.')

        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            Booking.objects.create(
                name=name,
                email=email,
                date=date,
                guests=guests,
                package=package_choice,
                special_requests=special_requests,
            )
            messages.success(
                request,
                f"🎉 Booking confirmed! Thank you, {name}! "
                f"We've received your booking for {guests} guest(s) on {date.strftime('%B %d, %Y')}. "
                f"A confirmation will be sent to {email}."
            )
            return redirect('booking')

    context = {
        'packages': packages,
        'min_date': datetime.date.today().isoformat(),
    }
    return render(request, 'bookings/booking.html', context)
