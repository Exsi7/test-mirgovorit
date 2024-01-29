from django.shortcuts import render
from test_mirgovorit_backend.recipe.models import Recipe, Product, Structure
from django.db.models import F
# Create your views here.
def add_product_view(request):
    if request.GET:
        param = request.GET
        recipe = Recipe.objects.get(pk=param.get('recipe_id'))
        product = recipe.products.get(pk=param.get('product_id'))
        weight = int(param.get('weight'))
        print(recipe, product, weight)
        if product:
            Structure.objects.filter(recipe=recipe, product=product).update(weight=weight)
        else:
            Structure.objects.create(recipe=recipe, product=product, weight=weight)

def cook_recipe_view(request):
    if request.GET:
        recipe_id = request.GET.get('recipe_id')
        Product.objects.filter(recipe__id=recipe_id).update(cook_recipe=F('cook_recipe') + 1)


def show_ricipes_without_product_view(request):
    if request.GET:
        product_id = int(request.GET.get('product_id'))
        print(product_id)
        recipes = Recipe.objects.exclude(products__id=product_id, structure__weight__gte=10)
        print(recipes)
        return render(request, 'index.html', context={'recipes': recipes})
