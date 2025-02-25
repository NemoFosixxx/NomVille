from django.urls import path
from recipes.views import *

urlpatterns = [
    path("", index_view, name="index"),
    path("add_recipe", add_recipe_view, name="add_recipe"),
]
