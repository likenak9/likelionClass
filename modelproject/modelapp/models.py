from django.db import models

# Create your models here.

# class 는 단어의 시작은 항상 대문자
class Blog(models.Model):
    title = models.CharField(max_length = 100) # input type = "text"
    body = models.TextField('내용') # text area
    created_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title
    
    