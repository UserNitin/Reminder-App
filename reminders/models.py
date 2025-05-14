from django.db import models
import datetime

class Reminder(models.Model):
    DELIVERY_CHOICES = [
        ('sms', 'SMS'),
        ('email', 'Email'),
    ]
    message = models.TextField()
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=datetime.time(0, 0))
    delivery_method = models.CharField(max_length=10, choices=DELIVERY_CHOICES, default='email')

    def __str__(self):
        return f"{self.delivery_method.upper()} at {self.date} {self.time}"
