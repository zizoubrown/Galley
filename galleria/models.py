from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category