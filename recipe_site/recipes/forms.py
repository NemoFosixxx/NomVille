from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description", "ingredients", "steps", "cook_time", "image"]
        
        labels = {
            "title": "Название",
            "description": "Описание",
            "ingredients": "Ингредиенты",
            "steps": "Шаги приготовления",
            "cook_time": "Время приготовления",
            "image": "Изображение",
        }

        help_texts = {
            "ingredients": "Введите список ингредиентов через запятую",
            "cook_time": "Укажите время в минутах",
        }
        
        
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})