from django.shortcuts import render, redirect, get_object_or_404
from assignment.models import Project, Task

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('Loginview')
    
    user = request.user
    projects = Project.objects.filter(assigned_to=user)

    # Update the status of each project based on task completion
    for project in projects:
        tasks = project.tasks.all()
        if tasks.exists() and all(task.status == "completed" for task in tasks):
            project.status = "completed"
        else:
            project.status = "pending"
        project.save()

    context = {
        'projects': projects,
    }
    return render(request, 'index.html', context)

def projectDetail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = project.tasks.all()
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='completed').count()
    progress = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0

    if request.method == "POST":
        task_id = request.POST.get("task_id")
        status = request.POST.get("status")
        task = get_object_or_404(Task, id=task_id, project=project)
        task.status = status
        task.save()
        return redirect('ProjectDetail', id=project.id)

    project.calculate_total_score()

    context = {
        "project": project,
        "tasks": tasks,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "progress": progress,
        "score": project.total_score,
        "status_choices": Task._meta.get_field('status').choices,
    }

    return render(request, 'prjdetail.html', context)
