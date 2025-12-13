from django.db import models

class Booking(models.Model):

    SERVICE_CHOICES = [
        ('deep_cleaning', 'Deep Cleaning'),
        ('move_in_out', 'Move-in / Move-out'),
        ('floor_care', 'Floor Care'),
    ]

    service_type = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )

    rooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()

    date = models.DateField()
    time = models.TimeField()

    address = models.TextField()

    calendar_event_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        default='booked'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_type} on {self.date} at {self.time}"
