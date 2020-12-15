from django.db import models


class Animal(models.Model):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'

    priority_choices = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    name = models.CharField(max_length=20, blank=False)
    image_url = models.URLField(blank=False)
    description = models.TextField(max_length=250, blank=False)
    priority = models.CharField(max_length=6, choices=priority_choices, default=LOW)
    is_cured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
