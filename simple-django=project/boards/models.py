from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=30,unique=True)
    description= models.CharField(max_length=150)

class Topic(models.Model):
    subject = models.CharField(max_length=200,)
    board= models.ForeignKey(Board,related_name='topic',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='topic1',on_delete=models.CASCADE)
    create_dt = models.DateField(auto_now_add=True)

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic,related_name='post',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='post1',on_delete=models.CASCADE)
    created_dt = models.DateField(auto_now_add=True)
