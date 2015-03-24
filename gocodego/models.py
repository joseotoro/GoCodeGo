from django.db import models
from django import forms
from django.contrib import admin

class Problem(models.Model):
    title = models.CharField(max_length=200)	
    description = models.TextField(max_length=2000)
    template = models.TextField(max_length=2000)
    test_cases = models.TextField(max_length=2000)
    category = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
 
@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'description', 'template', 'test_cases', 'pub_date')