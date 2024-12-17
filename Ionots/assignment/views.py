from django.shortcuts import render, redirect
from assignment.models import Project, Task

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('Loginview')
    
    return render(request, 'index.html')
