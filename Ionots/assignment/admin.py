from django.contrib import admin
from assignment.models import Project, Task

# TaskInline allows us to edit tasks directly within the Project admin
class TaskInline(admin.TabularInline):
    model = Task
    extra = 1  
    fields = ['task', 'points', 'status']  
    readonly_fields = ['project']  

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'assigned_to', 'status', 'deadline', 'date', 'total_score', 'marks']
    search_fields = ['title', 'assigned_to__username', 'status']  
    list_filter = ['status', 'assigned_to', 'deadline']
    ordering = ['-date']  
    inlines = [TaskInline]  
    readonly_fields = ('total_score',) 
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task)

