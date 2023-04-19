from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', "Хилы"),
        ('dd', "ДД"),
        ('buyers', 'Торговцы'),
        ('gildmaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    articleTime = models.DateTimeField(auto_now_add=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.CharField(max_length=11, choices=TYPE, default='tank')
    upload = models.FileField(upload_to='uploads/')

    def preview(self):
        return '{}...'.format(self.text[:123])

    def __str__(self):
        return f'{self.title.title()}: {self.text}. Автор: {self.author}, категория: {self.category}'


class UserResponse(models.Model):
    responseTime = models.DateTimeField(auto_now_add=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)