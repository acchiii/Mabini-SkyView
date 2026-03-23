from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    inclusions = models.TextField(blank=True, help_text="One inclusion per line")
    max_guests = models.IntegerField(default=10)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_inclusions_list(self):
        if self.inclusions:
            return [item.strip() for item in self.inclusions.split('\n') if item.strip()]
        return []

    class Meta:
        ordering = ['price']
