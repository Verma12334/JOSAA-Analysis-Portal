from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

    

    

class Extract(models.Model):
    id = models.IntegerField(primary_key=True)
    Institute = models.CharField(max_length=400)
    Seat_type = models.CharField(max_length=20)
    Gender = models.CharField(max_length=30)
    Opening_rank = models.CharField(max_length=10)
    Closing_rank = models.CharField(max_length=10)
    Year = models.IntegerField()
    Round = models.IntegerField()
    Program_name = models.CharField(max_length=150)
    Program_duration = models.IntegerField()
    Program_type = models.CharField(max_length=100)
    

    
    
    def __str__(self):
        return self.Program_name

