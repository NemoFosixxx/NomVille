# Generated by Django 5.1.6 on 2025-02-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='steps',
            field=models.JSONField(default=list, help_text='Список шагов приготовления'),
        ),
    ]
