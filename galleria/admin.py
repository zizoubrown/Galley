from django.contrib import admin
from .models import Image,Location,Category

admin.site.site_header = "Gallery Admin"
admin.site.site_title = "Gallery Admin Area"
admin.site.index_title = "Welcome to gallery admin"

# Register your models here.
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image)