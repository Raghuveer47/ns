# models.py
from django.db import models

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    people = models.PositiveIntegerField(null=True, blank=True)
    travel_date = models.DateField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

class AdminDecision(models.Model):
    show_modal = models.BooleanField(default=False)

    def __str__(self):
        return "Show Modal" if self.show_modal else "Do Not Show Modal"
