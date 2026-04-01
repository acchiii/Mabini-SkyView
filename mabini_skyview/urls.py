from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500, handler403
from core.views import custom_404, custom_500, custom_403


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('bookings/', include('bookings.urls')),
    path('gallery/', include('gallery.urls')),
    path('packages/', include('packages.urls')),
]
if True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
handler404 = custom_404
handler500 = custom_500
handler403 = custom_403

