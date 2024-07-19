from django.db import models

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    people = models.PositiveIntegerField(null=True, blank=True)  # Optional field
    travel_date = models.DateField(null=True, blank=True)  # Optional field
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} on {self.submitted_at}"
