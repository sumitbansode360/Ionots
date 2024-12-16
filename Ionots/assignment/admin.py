from django.contrib import admin
from assignment.models import Project, Task

# TaskInline allows us to edit tasks directly within the Project admin
class TaskInline(admin.TabularInline):  # You can use TabularInline or StackedInline based on your preference
    model = Task
    extra = 1  # This adds an empty row for adding a new task.
    fields = ['task', 'points', 'status']  # Fields to be displayed for each task inline
    # You can add 'project' field as read-only if it's set automatically
    readonly_fields = ['project']  # Read-only to show the related project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'assigned_to', 'status', 'deadline', 'date', 'total_score']
    search_fields = ['title', 'assigned_to__username', 'status']  # Search by project title, user, and status
    list_filter = ['status', 'assigned_to', 'deadline']  # Filters for easier project management
    ordering = ['-date']  # Order projects by creation date (latest first)
    inlines = [TaskInline]  # Link TaskInline to the ProjectAdmin

    # Optionally, you can add actions or methods to the admin
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Optionally, add custom filters or logic here to customize how projects are shown.
        return queryset

# Register your models in the Django admin
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task)
