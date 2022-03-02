from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255, )
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, )

    class Meta:
        verbose_name = "Пост"
        verbose_name = "Посты"
    
    def __str__(self):
        return f'{self.title} {self.user}'