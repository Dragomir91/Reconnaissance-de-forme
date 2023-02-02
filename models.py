from email.policy import default
from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin


class Login(models.Model):
    name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    

class Persone(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age_name = models.IntegerField(default = 0)
    
class Question(models.Model):
  
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def __str__(self):
        return self.question_text


class Choice(models.Model):
  
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #release_date = models.DateField()


# Create your models here.
