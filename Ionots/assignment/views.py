from django.shortcuts import render
from assignment.models import Project, Task
# Create your views here.

def index(request):
    return render(request, 'index.html')
