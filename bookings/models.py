from django.db import models


class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateField()
    guests = models.IntegerField()
    package = models.CharField(max_length=200, blank=True, null=True)
    special_requests = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} ({self.guests} guests)"

    class Meta:
        ordering = ['-created_at']
