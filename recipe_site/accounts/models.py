from django.contrib.auth.models import AbstractUser
from django.db import models

# class CustomUser(AbstractUser):
#     username = models.CharField(
#         max_length=16, 
#         unique=True, 
#         help_text="Обязательное поле. Не более 16 символов. Только буквы, цифры и символы @/./+/-/_."
#     )