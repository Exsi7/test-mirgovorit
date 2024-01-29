from django.contrib import admin
from .models import Recipe, Product, Structure
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Product)
admin.site.register(Structure)

