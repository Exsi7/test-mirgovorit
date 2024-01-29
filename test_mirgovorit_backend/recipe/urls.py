from django.contrib import admin
from django.urls import path
from test_mirgovorit_backend.recipe import views

urlpatterns = [
    path('add_product_recipe', views.add_product_view),
    path('cook_recipe', views.cook_recipe_view),
    path('show_recipes_without_product', views.show_ricipes_without_product_view),
]