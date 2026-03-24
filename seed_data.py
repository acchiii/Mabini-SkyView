import os
import django
from decouple import config

# 1️⃣ Set the settings module first
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mabini_skyview.settings')

# 2️⃣ Setup Django
django.setup()

# 3️⃣ Now import your models safely
from packages.models import Package
from django.contrib.auth.models import User

print("Seeding Mabini SkyView database...")

packages_data = [
    {"name": "Day Tripper", "price": "350.00", "description": "Ideal for a solo visit...", "inclusions": "Entrance fee & trail pass\nViewpoint deck access\nWelcome refreshment\nFree parking", "max_guests": 10, "is_featured": False},
    {"name": "SkyView Explorer", "price": "650.00", "description": "Our bestselling full-day package...", "inclusions": "Full-day entrance & trail access\nGuided nature hike (2 hrs)\nFilipino lunch buffet\nViewpoint & photography spots\nBonfire session (evening)\nFree parking & shuttle", "max_guests": 20, "is_featured": True},
    {"name": "Summit Celebration", "price": "1200.00", "description": "The ultimate SkyView experience...", "inclusions": "Private event venue (up to 50 pax)\nFull-day exclusive access\nCatered 3-course dinner\nSunset viewing session\nLive acoustic music (2 hrs)\nDedicated event coordinator", "max_guests": 50, "is_featured": False},
    {"name": "Sunrise Serenity", "price": "450.00", "description": "An early-bird package...", "inclusions": "Early access from 5:00 AM\nSunrise viewpoint access\nFilipino breakfast set\nHot coffee or tea\nTrail access until noon", "max_guests": 15, "is_featured": False},
    {"name": "Family Fun Day", "price": "500.00", "description": "A wholesome family package...", "inclusions": "Full-day entrance for family (2 adults + 2 kids)\nKids activity zone access\nFamily picnic set\nGuided nature walk\nFree parking", "max_guests": 8, "is_featured": False},
    {"name": "Corporate Retreat", "price": "900.00", "description": "Team-building package...", "inclusions": "Private function hall (half-day)\nTeam-building activities\nFull catered lunch\nCoffee & snack breaks\nVIP viewpoint access\nCertificate of participation", "max_guests": 30, "is_featured": False},
]

# Create packages
for data in packages_data:
    pkg, created = Package.objects.get_or_create(name=data["name"], defaults=data)
    status = "Created" if created else "Already exists"
    print(f"{status}: {pkg.name} (₱{pkg.price})")

# Create superuser if it doesn’t exist
if not User.objects.filter(username=config('admin')).exists():
    User.objects.create_superuser(config('admin'), config('adminemail'), config('adminpass'))
    print("Superuser created: admin / skyview2024")
else:
    print("Superuser 'admin' already exists")

print("✅ Database seeded successfully!")