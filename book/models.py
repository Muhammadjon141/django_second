from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    author = models.CharField(max_length=50, null=False)
    count = models.PositiveIntegerField()
    price = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)