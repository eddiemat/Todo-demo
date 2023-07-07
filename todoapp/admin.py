from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdminDetailedDisplay(admin.ModelAdmin):
    list_display=('taskName', 'created_at', 'updated_at', 'is_completed')
    search_fields=('taskName',)

admin.site.register(Task, TaskAdminDetailedDisplay)
