from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class GetOrNoneManager(models.Manager):
    """Adds get_or_none method to objects"""
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None

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
    pub_date = models.DateTimeField('last modification')
    checked = models.BooleanField(default=False)

    objects = GetOrNoneManager()

    def __str__(self):
        return str(self.problem) + ' - ' + self.user.username
 
@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'description', 'template', 'test_cases', 'pub_date')

@admin.register(ProblemSolution)
class ProblemSolutionAdmin(admin.ModelAdmin):
    pass