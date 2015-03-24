from django.db import models
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User

class Problem(models.Model):
    title = models.CharField(max_length=200)	
    description = models.TextField(max_length=2000)
    template = models.TextField(max_length=2000)
    test_cases = models.TextField(max_length=2000)
    category = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class ProblemSolution(models.Model):
    user = models.ForeignKey(User)
    problem = models.ForeignKey(Problem)
    solution = models.TextField(max_length=2000)
    votes = models.ManyToManyField(User, related_name='votes')
 
@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'description', 'template', 'test_cases', 'pub_date')