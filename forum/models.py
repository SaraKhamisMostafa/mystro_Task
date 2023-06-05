from django.db import models

# Create your models here.
class Forum(models.Model):
    question=models.CharField(max_length=1000)
    answer=models.TextField(max_length=10000)
class Question(models.Model):
         
    