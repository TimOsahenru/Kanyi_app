from django.contrib import admin
from .models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']


admin.site.register(Task, TaskAdmin)
