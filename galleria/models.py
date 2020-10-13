from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

    def save_location(self):
        salf.save()

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    @classmethod
    def search_by_category(cls,search_term):
        search_result = cls.objects.filter(category_icontains=search_term)
        return search_result