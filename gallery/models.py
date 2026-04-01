from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=300)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    # Optimized thumbnails - auto-generated
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(400, 400)],
        format='JPEG',
        options={'quality': 85, 'optimize': True, 'progressive': True}
    )
    
    medium = ImageSpecField(
        source='image',
        processors=[ResizeToFill(800, 800)],
        format='JPEG',
        options={'quality': 85, 'optimize': True, 'progressive': True}
    )
    
    # Full size for lightbox (slightly compressed)
    full = ImageSpecField(
        source='image',
        processors=[],
        format='JPEG',
        options={'quality': 90, 'optimize': True, 'progressive': True}
    )

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ['-uploaded_at']
