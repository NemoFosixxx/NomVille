from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from recipes.models import Recipe
from .forms import RecipeForm
import random


def index_view(request):
    recipes = list(Recipe.objects.all())
    random_recipes = random.sample(recipes, min(len(recipes), 5))
    return render(request, "recipes/index.html", {"recipes": random_recipes})

def recipe_details_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    steps = recipe.steps.split("|") 
    return render(request, "recipes/recipe_details.html", {"recipe": recipe, "steps": steps})

@login_required
def add_recipe_view(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.steps = request.POST.get("steps", "")
            recipe.save()
            return redirect("recipe_details", recipe_id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, "recipes/add_recipe.html", {"form": form})

@login_required
def edit_recipe_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)
    
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe_details", recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, "recipes/edit_recipe.html", {"form": form, "recipe": recipe})

@login_required
def delete_recipe_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)
    
    if request.method == 'POST':
        recipe.delete()
        return redirect('index')
    return redirect('recipe_details', recipe_id=recipe.id)