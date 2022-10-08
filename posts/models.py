from user.models import User
from django.db import models


class Post(models.Model):
    
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='заголовок')
    content = models.TextField(blank=False, null=False, verbose_name='текст')
    image = models.ImageField(upload_to='photo', null=False, blank=False, verbose_name='фотографии')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_updata = models.DateTimeField(auto_now=True, verbose_name='время обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.text

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
