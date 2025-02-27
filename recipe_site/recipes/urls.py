from django.urls import path
from recipes.views import *

urlpatterns = [
    path("", index_view, name="index"),
    path("add_recipe/", add_recipe_view, name="add_recipe"),
    path("recipe/<int:recipe_id>/", recipe_details_view, name="recipe_details"),
    path("recipe/<int:recipe_id>/edit/", edit_recipe_view, name="edit_recipe"),
    path("recipe/<int:recipe_id>/delete/", delete_recipe_view, name="delete_recipe"),
]
