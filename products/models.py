from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    title = models.CharField(max_length = 80)
    description = models.CharField(max_length=200)
    price = models.PositiveIntegerField(
        validators = [MinValueValidator(1)]
    )
    is_subscription = models.BooleanField(default = False)
    duration_days = models.SmallIntegerField(null = True, blank = True)


    def __str__(self):
        return f"{self.title}"