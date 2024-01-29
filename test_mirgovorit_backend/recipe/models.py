from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    cook_recipe = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, blank=True, through="Structure")


    def __str__(self):
        return self.name


class Structure(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField(blank=False)