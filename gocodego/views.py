from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import logout as auth_logout

from models import Problem, ProblemSolution


def index(request):
	return render(request, 'index.html')

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')

def detail(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)

    solved = False
    if request.user.is_authenticated():
        solved = ProblemSolution.objects.get_or_none(problem=problem, user=request.user) is not None

    return render(request, 'problem/detail.html', {'problem': problem, 'solved': solved})

def problems(request):
    prob_solved = []
    if request.user.is_authenticated():
        prob_solved = ProblemSolution.objects.filter(user=request.user)
        prob_solved = map(lambda prob: prob.id, prob_solved)
    
    return render(request, 'problem/list.html', {'problems': Problem.objects.all, 'solved': prob_solved})


def profile(request):
    if not request.user.is_authenticated():
	   return HttpResponseRedirect('/login/google-oauth2/')

    prob_solved = ProblemSolution.objects.filter(user=request.user).count()
    points = prob_solved * 10

    return render(request, 'profile.html', {'problems': prob_solved, 'points': points})