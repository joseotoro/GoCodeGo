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

    if request.user.is_authenticated():
        solved = ProblemSolution.objects.get_or_none(problem=problem, user=request.user)
        if solved is not None:
            solution = solved.solution
            return render(request, 'problem/detail.html', {'problem': problem, 'solved': True, 'solution': solution})

    return render(request, 'problem/detail.html', {'problem': problem, 'solved': False})

def problems(request):
    prob_solved = []
    if request.user.is_authenticated():
        prob_solved = ProblemSolution.objects.filter(user=request.user)
        prob_solved = map(lambda prob: prob.problem.id, prob_solved)
    
    return render(request, 'problem/list.html', {'problems': Problem.objects.all, 'solved': prob_solved})

def search(request):
    if 'search' not in request.POST:
        return problems(request)

    name = request.POST['search']
    prob_solved = []
    probs = Problem.objects.filter(title__icontains=name)
    if request.user.is_authenticated():
        prob_solved = ProblemSolution.objects.filter(user=request.user)
        prob_solved = map(lambda prob: prob.problem.id, prob_solved)
    
    return render(request, 'problem/list.html', {'problems': probs.all, 'solved': prob_solved})

def profile(request):
    if not request.user.is_authenticated():
	   return HttpResponseRedirect('/login/google-oauth2/')

    prob_solved = map(lambda prob: prob.problem.id, ProblemSolution.objects.filter(user=request.user))
    problems_cat = map(lambda prob: prob.category, Problem.objects.filter(id__in=prob_solved))
    points = 0

    for p in problems_cat:
        print p
        if p == "Starter":
            points += 10
        elif p == "Easy":
            points += 50
        elif p == "Medium":
            points += 250
        elif p == "Hard":
            points += 2000

    return render(request, 'profile.html', {'problems': len(prob_solved), 'points': points})