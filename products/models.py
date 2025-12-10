from django.db import models

class Product(models.Model):
    title = models.CharField(max_length = 80)
    description = models.CharField()
    price = models.PositiveIntegerField()
    is_subscription = models.BooleanField(default = False)
    duration_days = models.SmallIntegerField(null = True, blank = True)


    def __str__(self):
        return f"{self.title}"