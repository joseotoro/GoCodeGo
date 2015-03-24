from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from models import Problem, ProblemSolution

@login_required
def check(request):
    if request.is_ajax() and request.user.is_authenticated():
        code =  request.POST['code']
        problem_id = int(request.POST['problem'])

        solved = ProblemSolution.objects.get_or_none(problem=problem_id, user=request.user) is not None
        
        if not solved:
            problem_testcode = Problem.objects.get(id=problem_id).test_cases
            code = code + 'int main() {' + problem_testcode + '}'

        return HttpResponse('asdads')
    else:
        return HttpResponse('')
