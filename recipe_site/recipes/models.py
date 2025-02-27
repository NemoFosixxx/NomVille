from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    cook_time = models.IntegerField()
    image = models.ImageField(upload_to="recipes/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # def get_steps(self):
    #     try:
    #         return json.loads(self.steps)
    #     except json.JSONDecodeError:
    #         return []

    # def set_steps(self, steps):
    #     self.steps = json.dumps(steps)
