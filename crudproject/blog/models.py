from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField('제목', max_length = 50)
    body = models.TextField('내용')
    nickname = models.CharField('닉네임', max_length = 30)
    created_at = models.DateTimeField('작성 시간', auto_now=True)
    