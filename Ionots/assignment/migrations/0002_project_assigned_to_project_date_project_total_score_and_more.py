# Generated by Django 4.2.7 on 2024-12-16 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=20),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('points', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=20)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='assignment.project')),
            ],
        ),
    ]
