from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100, blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50,  blank=False, null=False)

def __str__(self) :
    return f"{self.first_name} {self.last_name}"