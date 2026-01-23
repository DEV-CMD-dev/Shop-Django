from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    title = models.CharField(max_length = 80)
    description = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )
    price = models.PositiveIntegerField(
        validators = [MinValueValidator(1)]
    )
    is_subscription = models.BooleanField(default = False)
    duration_days = models.SmallIntegerField(null = True, blank = True)


    def __str__(self):
        return f"{self.title}"

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "product")
