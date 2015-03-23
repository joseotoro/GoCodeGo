from django.db import models
from django import forms
from django.contrib import admin

class Problem(models.Model):
    title = models.CharField(max_length=200)	
    description = models.CharField(max_length=2000)
    template = models.CharField(max_length=2000)
    test_cases = models.CharField(max_length=2000)
    category = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
 

class ProblemForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    template = forms.CharField(widget=forms.Textarea)
    test_cases = forms.CharField(widget=forms.Textarea)
    category = forms.CharField()
    pub_date = forms.DateTimeField()

    class Meta:
        model = Problem 

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    form = ProblemForm