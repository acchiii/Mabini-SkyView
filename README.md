# 🏔️ Mabini SkyView — Django Tourist Website

A full-stack Django website for **Mabini SkyView**, a scenic tourist destination in Mabini, Cebu City, Philippines. Built with Django 4.2, Django Templates, and Tailwind CSS (CDN).

---

## ✨ Features

- **Responsive** mobile-first design across all devices
- **Sticky glass navbar** with active link highlighting
- **Hero section** with parallax background, stats strip, and CTA
- **Amenities section** with hover-effect cards
- **Gallery** with masonry grid + full lightbox (keyboard navigable)
- **Packages** page with featured badges + FAQ accordion
- **Booking form** with server-side validation, success/error messages
- **Contact form** with Google Maps embed
- **About page** with image collage, vision/mission, values
- **Django Admin** panel for managing bookings, gallery, and packages
- **Sample data seeder** with 6 packages + admin user

---

## 🗂️ Project Structure

```
mabini_skyview/
├── manage.py
├── requirements.txt
├── setup.sh                      # Quick setup script
├── seed_data.py                  # Populate DB with sample data
│
├── mabini_skyview/               # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/                         # Homepage, About, Contact
│   ├── models.py                 # ContactMessage model
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── bookings/                     # Booking form & management
│   ├── models.py                 # Booking model
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── gallery/                      # Photo gallery
│   ├── models.py                 # GalleryImage model
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── packages/                     # Tour packages
│   ├── models.py                 # Package model
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
│   ├── base.html                 # Base layout (navbar + footer)
│   ├── core/
│   │   ├── home.html             # Homepage
│   │   ├── about.html            # About page
│   │   └── contact.html          # Contact page
│   ├── bookings/
│   │   └── booking.html          # Booking form
│   ├── gallery/
│   │   └── gallery.html          # Photo gallery
│   └── packages/
│       └── packages.html         # Packages listing
│
└── static/                       # Static assets folder
```

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.9 or higher
- pip
- Terminal / Command Prompt

### Option A — Automated Setup (Recommended)

```bash
# 1. Clone or extract the project
cd mabini_skyview

# 2. Run the setup script
bash setup.sh

# 3. Start the server
source venv/bin/activate
python manage.py runserver
```

### Option B — Manual Setup

```bash
# 1. Navigate to project folder
cd mabini_skyview

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate       # macOS/Linux
# OR: venv\Scripts\activate    # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Seed sample data (packages + admin user)
python seed_data.py

# 6. Start the development server
python manage.py runserver
```

### 7. Open in browser
```
Website:    http://127.0.0.1:8000
Admin:      http://127.0.0.1:8000/admin
Username:   admin
Password:   skyview2024
```

---

## 📦 Django Models

### `Booking` (bookings/models.py)
| Field | Type | Notes |
|-------|------|-------|
| name | CharField(200) | Guest full name |
| email | EmailField | Guest email |
| date | DateField | Visit date |
| guests | IntegerField | Number of guests |
| package | CharField(200) | Selected package (optional) |
| special_requests | TextField | Optional notes |
| status | CharField | Pending / Confirmed / Cancelled |
| created_at | DateTimeField | Auto-set on creation |

### `GalleryImage` (gallery/models.py)
| Field | Type | Notes |
|-------|------|-------|
| image | ImageField | Uploaded to `media/gallery/` |
| caption | CharField(300) | Image description |
| uploaded_at | DateTimeField | Auto-set on upload |

### `Package` (packages/models.py)
| Field | Type | Notes |
|-------|------|-------|
| name | CharField(200) | Package name |
| price | DecimalField | Per-person price |
| description | TextField | Full description |
| inclusions | TextField | One inclusion per line |
| max_guests | IntegerField | Max group size |
| is_featured | BooleanField | Show "Popular" badge |
| created_at | DateTimeField | Auto-set on creation |

### `ContactMessage` (core/models.py)
| Field | Type | Notes |
|-------|------|-------|
| name | CharField(200) | Sender name |
| email | EmailField | Sender email |
| subject | CharField(300) | Message subject |
| message | TextField | Message body |
| created_at | DateTimeField | Auto-set on creation |

---

## 🔑 Admin Panel

Access at `http://127.0.0.1:8000/admin` with `admin` / `skyview2024`.

**What you can manage:**
- **Bookings** — View, filter by status/date, update booking status inline
- **Gallery Images** — Upload photos with captions; they appear on the Gallery page
- **Packages** — Create/edit tour packages with inclusions; toggle featured status
- **Contact Messages** — Read messages sent through the Contact form

---

## 🖼️ Adding Gallery Images

1. Log into Admin: `http://127.0.0.1:8000/admin`
2. Go to **Gallery → Gallery Images → Add**
3. Upload an image file and enter a caption
4. Save — it will appear on the Gallery page immediately

---

## 🎨 Design Highlights

| Feature | Implementation |
|---------|---------------|
| Fonts | Playfair Display (headings) + DM Sans (body) |
| Colors | Slate-950 dark base, Teal-500 accent, Cyan highlights |
| Tailwind | Via CDN with custom config (extended colors, fonts, animations) |
| Icons | Lucide Icons (via CDN) |
| Images | Unsplash/Picsum placeholders (replace with real photos) |
| Animations | CSS keyframes: fadeUp, fadeIn; hover: card-lift, img-overlay |
| Lightbox | Vanilla JS with keyboard arrow navigation + ESC to close |
| Map | Google Maps embed (dark-inverted CSS filter for dark theme) |

---

## 🌐 Pages & URLs

| URL | Page | View |
|-----|------|------|
| `/` | Homepage | `core.views.home` |
| `/about/` | About Us | `core.views.about` |
| `/gallery/` | Photo Gallery | `gallery.views.gallery` |
| `/packages/` | Tour Packages | `packages.views.packages` |
| `/bookings/` | Book Now | `bookings.views.booking` |
| `/contact/` | Contact Us | `core.views.contact` |
| `/admin/` | Django Admin | Built-in |

---

## 🚀 Going to Production

1. Set `DEBUG = False` in `settings.py`
2. Change `SECRET_KEY` to a secure random value
3. Configure `ALLOWED_HOSTS` with your domain
4. Set up a production database (PostgreSQL recommended)
5. Serve static/media files via Nginx or WhiteNoise
6. Use Gunicorn as the WSGI server

```bash
pip install gunicorn whitenoise psycopg2-binary
gunicorn mabini_skyview.wsgi:application --bind 0.0.0.0:8000
```

---

## 📸 Replacing Placeholder Images

Hero and gallery sections use Unsplash URLs. Replace with real SkyView photos:

1. Add images via Admin → Gallery → Gallery Images
2. For hero/about backgrounds, update the `<img src="...">` in the templates:
   - `templates/core/home.html` — Hero and CTA section backgrounds
   - `templates/core/about.html` — Page header and collage images

---

## 📞 Contact Info in Templates

To update the default contact info, search for these in the templates:
- Phone: ``
- Email: ``
- Address: `Mabini, Cebu City, Cebu, Philippines 6000`

---

## 📄 License

This project is for the exclusive use of Mabini SkyView. All rights reserved.
