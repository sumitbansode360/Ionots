# models.py

from django.db import models
from userauths.models import User  # Assuming User is defined here

# Status Choices
STATUS_CHOICES = (
    ("pending", "Pending"),
    ("completed", "Completed"),
)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    deadline = models.DateField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects', null=True)
    total_score = models.IntegerField(default=0)  # To store the total score of the project
    def __str__(self):
        return self.title
    
    def calculate_total_score(self):
        total = sum(task.points for task in self.tasks.filter(status='completed'))
        self.total_score = total
        self.save()

    # Calculate the progress of the project
    def calculate_progress(self):
        total_tasks = self.tasks.count()
        if total_tasks == 0:
            return 0  # If there are no tasks, progress is 0%
        completed_tasks = self.tasks.filter(status='completed').count()
        progress = (completed_tasks / total_tasks) * 100
        return progress


class Task(models.Model):
    task = models.CharField(max_length=200, null=False)
    points = models.IntegerField(null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')  # Link task to project

    def __str__(self):
        return self.task
