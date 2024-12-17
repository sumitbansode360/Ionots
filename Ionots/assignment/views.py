from django.shortcuts import render, redirect
from assignment.models import Project, Task

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('Loginview')
    
    user = request.user
    projects = Project.objects.filter(assigned_to=user)

    context = {
        'projects' : projects
    }
    return render(request, 'index.html', context)

def projectDetail(request, id):
    # if not request.user.is_authenticated:
    #     return redirect('Loginview')
    
    # user = request.user
    # projects = Project.objects.filter(assigned_to=user)
    return render(request, 'prjdetail.html')


