from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import logout as auth_logout

from models import Problem


def index(request):
	return render(request, 'index.html')

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')

def problem(request, problem_id):
	problem = get_object_or_404(Problem, pk=problem_id)
	return render(request, 'problem/detail.html', {'problem': problem})