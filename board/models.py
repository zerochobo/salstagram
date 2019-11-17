from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    key = models.CharField(max_length=50)    # 글 삭제 시 확인할 키값 기본적으로 default=123으로 구현함.
    author = models.CharField(max_length=50)    # 익명성을 위해 CharField 로 구현
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created', ]

    def get_absolute_url(self):
        return reverse('board:detail', args=[self.id])
