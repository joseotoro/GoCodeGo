from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import logout as auth_logout

from models import Problem, ProblemSolution, User
from forms import UserForm


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
            return render(request, 'problem/detail.html', { 'problem': problem, 'solved': solved.checked, 'load': solved is not None, 'solution': solution })

    return render(request, 'problem/detail.html', {'problem': problem, 'solved': False, 'load': False })

def problems(request):
    prob_solved = []
    if request.user.is_authenticated():
        prob_solved = ProblemSolution.objects.filter(user=request.user, checked=True)
        prob_solved = map(lambda prob: prob.problem.id, prob_solved)
    

    categories = ['Starter', 'Easy', 'Medium', 'Hard']
    probs = list(Problem.objects.all())
    probs.sort(key=lambda t: categories.index(t.category))

    return render(request, 'problem/list.html', {'problems': probs, 'solved': prob_solved})

def search(request):
    if 'search' not in request.POST:
        return problems(request)

    name = request.POST['search']
    prob_solved = []

    categories = ['Starter', 'Easy', 'Medium', 'Hard']
    probs = list(Problem.objects.filter(title__icontains=name))
    probs.sort(key=lambda t: categories.index(t.category))

    if request.user.is_authenticated():
        prob_solved = ProblemSolution.objects.filter(user=request.user)
        prob_solved = map(lambda prob: prob.problem.id, prob_solved)
    
    return render(request, 'problem/list.html', {'problems': probs, 'solved': prob_solved})

def user_points(user):
    user = get_object_or_404(User, username=user)

    prob_solved = map(lambda prob: prob.problem.id, ProblemSolution.objects.filter(user=user, checked=True))
    problems_cat = map(lambda prob: prob.category, Problem.objects.filter(id__in=prob_solved))
    points = 0

    for p in problems_cat:
        if p == "Starter":
            points += 10
        elif p == "Easy":
            points += 50
        elif p == "Medium":
            points += 250
        elif p == "Hard":
            points += 2000

    return (len(prob_solved), points)

def users(request):
    users = map(lambda u: u.username, list(User.objects.all()))
    users = map(lambda u: (u, user_points(u)[1]), users)
    users.sort(key=lambda u: u[1], reverse=True)

    return render(request, 'profile/list.html', {'users': users})


def user(request, user):
    user = get_object_or_404(User, username=user)

    (problems, points) = user_points(user.username)

    return render(request, 'profile/profile.html', {'u': user, 'problems': problems, 'points': points})

def profile_edit(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    return render(request, 'profile/edit.html')

def profile_save(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = UserForm(request.POST)

        username = request.POST['username'].replace(' ', '').strip()
        user_error = None
        user = None

        try:
           user =  User.objects.get(username=username)
        except User.DoesNotExist:
           pass
        
        if user is not None and user.username.lower() != request.user.username.lower():
            user_error = 'Username is already taken!'
        if form.is_valid() and user_error is None:
            request.user.username = username
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.bio = form.cleaned_data['bio']
            request.user.website = form.cleaned_data['website']
            request.user.facebook = form.cleaned_data['facebook']
            request.user.twitter = form.cleaned_data['twitter']
            request.user.linkedin = form.cleaned_data['linkedin']
            request.user.github = form.cleaned_data['github']

            request.user.save()

            return render(request, 'profile/edit.html', {'ok': 'Changes saved!'})
        else:
            return render(request, 'profile/edit.html', {'ok': None, 'errors': form.errors, 'user_error': user_error})

    return HttpResponseRedirect('/profile/edit/')