from django.contrib import admin
from models import User, Problem, ProblemSolution, Friendship, Notification, Message

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'description', 'template', 'test_cases', 'pub_date')

@admin.register(ProblemSolution)
class ProblemSolutionAdmin(admin.ModelAdmin):
    pass

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    pass

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass