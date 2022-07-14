from django.forms import ModelForm
from .models import Task


class TaskEdit(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

