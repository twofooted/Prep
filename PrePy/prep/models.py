from django.db import models

class Recipe(models.Model):
    
    MEAL_CHOICES = (
        ('dinner', 'Dinner'),
        ('lunch', 'Lunch'),
        ('breakfast', 'Breakfast'),
        ('dessert', 'Dessert'),
        ('drink', 'Drinks / Spirits')
    )

    name = models.CharField(max_length=100)
    meal = models.CharField(max_length=100, choices=MEAL_CHOICES)
    plan_for = models.DateField()

    def __str__(self):
        return self.name
