from typing import Any
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    author = models.CharField(max_length=50, null=False)
    count = models.PositiveIntegerField()
    price = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title, self.description, self.author, self.count, self.price, self.create_date

class Authors(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=50, null=False)
    autobiorophy = models.TextField()
    birth_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.first_name, self.last_name, self.autobiorophy, self.birth_date, self.create_date