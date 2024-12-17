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
from django.shortcuts import render, get_object_or_404
from .models import Project

def projectDetail(request, id):
    # Fetch the project by ID, or return 404 if not found
    project = get_object_or_404(Project, id=id)

    # Fetch the tasks associated with the project
    tasks = project.tasks.all()

    # Calculate progress and completed tasks count
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='completed').count()
    progress = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0

    # Calculate the total score
    project.calculate_total_score()

    # Context to pass to the template
    context = {
        "project": project,
        "tasks": tasks,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "progress": progress,
        "score": project.total_score,
    }

    return render(request, 'prjdetail.html', context)
