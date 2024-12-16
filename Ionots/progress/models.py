from django.db import models
from assignment.models import Project
# Create your models here.

class Progress(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='progress')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    tasks_completed = models.IntegerField(default=0)
    total_tasks = models.IntegerField(default=1)
    score = models.FloatField(default=0.0)