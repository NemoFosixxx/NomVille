from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from recipes.models import Recipe
import random


def index_view(request):
    return render(request, "recipes/index.html")

def add_recipe_view(request):
    return render(request, "recipes/add_recipe.html")