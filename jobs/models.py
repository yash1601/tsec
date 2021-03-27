from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#salary is in lpa

class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    text = models.TextField()
    url = models.URLField()
    
    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    url = models.URLField()

    def __str__(self):
        return self.title

class Job(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    company = models.CharField(max_length=200, null=False, blank=False)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    salary = models.IntegerField(null=False, blank=False)
    url = models.URLField()
    articles = models.ManyToManyField(Article, blank = True)
    questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return f"{self.title} at {self.company}"


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jobs = models.ManyToManyField(Job, blank=True)
    solved = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.user.username


