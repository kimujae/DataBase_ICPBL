from django.db import models
from common.models import User, UserProfile

# Create your models here.


class Car(models.Model):
    CAR_TYPES = [
        ('LI', 'Light'),
        ('S', 'Small'),
        ('SC', 'Subcompact'),
        ('C', 'Compact'),
        ('LA', 'Large'),
        ('SUV', 'SUV'),
        ('V', 'Van')

    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    num = models.CharField(max_length=6, primary_key = True)
    model = models.CharField(max_length=6)
    reg_date = models.DateTimeField(auto_now=True)
    approve = models.BooleanField(default=False)
    car_type = models.CharField(choices=CAR_TYPES, max_length=10)
    entry_time = models.DateTimeField(auto_now=True)
    exit_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['reg_date']

    def __str__(self):
        return self.num

class Park(models.Model):
    BUILDING_NUM_CHOICES = (
        (101, '101동'),
        (102, '102동'),
        (103, '103동'),
        (104, '104동'),
        (105, '105동'),
        (106, '106동'),
        (107, '107동'),
    )
    PARK_TYPES = [
        ('G', 'General'),
        ('D', 'Disabled'),
        ('E', 'Electric')
    ]
    location = models.IntegerField(choices=BUILDING_NUM_CHOICES, default="")
    car =  models.ForeignKey(Car, on_delete=models.CASCADE, null = True, blank = True)
    row = models.CharField(max_length=1)
    column = models.IntegerField()
    park_type = models.CharField(choices=PARK_TYPES, max_length=8)

    class Meta:
        ordering = ['row', 'column']

    def __str__(self):
        return self.id
# Create your models here.
