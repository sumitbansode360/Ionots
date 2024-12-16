from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    status = models.CharField(max_length=20, choices=[('Assigned', 'Assigned'), ('Accepted', 'Accepted')], default='Assigned')
    deadline = models.DateField()
