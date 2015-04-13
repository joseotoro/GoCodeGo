from django.db import models
from django.contrib.auth.models import AbstractUser

ICON_CHOICES = (
    (0, 'info'),
    (1, 'success'),
    (2, 'warning'),
    (3, 'danger'),
)

FRIENDSHIP_CHOICES = (
    (0, 'PENDING'),
    (1, 'OK'),
    (2, 'BLOCKED'),
)

class GetOrNoneManager(models.Manager):
    """Adds get_or_none method to objects"""
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None

class User(AbstractUser):
    bio = models.TextField(max_length=150, null=True)
    twitter = models.CharField(max_length=80, null=True)
    github = models.CharField(max_length=80, null=True)
    linkedin = models.CharField(max_length=80, null=True)
    facebook = models.CharField(max_length=80, null=True)
    website = models.CharField(max_length=150, null=True)

class Friendship(models.Model):
    source = models.ForeignKey(User, related_name='source')
    target = models.ForeignKey(User, related_name='target')
    accepted = models.IntegerField(choices=FRIENDSHIP_CHOICES)

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')
    message = models.TextField(max_length=300)
    read = models.BooleanField(default=False)

class Notification(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField('notification date')
    message = models.CharField(max_length=300)
    icon = models.IntegerField(choices=ICON_CHOICES)

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

