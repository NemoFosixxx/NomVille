# Generated by Django 5.1.6 on 2025-02-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_cook_time_alter_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(related_name='recipes', to='recipes.category'),
        ),
    ]
