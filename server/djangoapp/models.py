from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    
    # Additional fields can be added here as needed
    
    def __str__(self):
        return self.name

# Car Model model
class CarModel(models.Model):

    CAR_TYPE_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]
    
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Foreign key to CarMake
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES, default='SUV')
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )
    
    # Additional fields can be added here as needed
    
    def __str__(self):
        return f"{self.name} ({self.car_make.name}) - {self.year}"
