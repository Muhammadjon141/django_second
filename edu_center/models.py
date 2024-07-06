from typing import Any
from django.db import models
from .helpers import Save_image
# Create your models here.
class Authors(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=50, null=False)
    autobiorophy = models.TextField()
    birth_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.first_name, self.last_name, self.autobiorophy, self.birth_date, self.create_date}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to=Save_image.save_image)
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.title, self.description, self.author, self.count, self.price, self.create_date}"

    def full_name(self):
        return f"{self.title} {self.price}"
    
class User(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    user_name = models.CharField(max_length=50, null=False)
    birth_date = models.DateField()
    create_time = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.user_name} {self.birth_date} {self.create_time}"

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.user} {self.book} {self.comment} {self.create_time}"
    
    def full_info(self) -> str:
        return f"{self.comment[:10:]} to {self.book.title}"