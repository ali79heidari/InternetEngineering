from django.db import models

from accounts.models import CustomUser


class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    calorie = models.PositiveIntegerField(default=0)
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class SelectFoodItem(models.Model):
    option = (
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('snacks', 'snacks'),
    )
    name = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=option)
    quantity = models.PositiveIntegerField(default=1)
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
