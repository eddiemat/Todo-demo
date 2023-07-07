from django import forms
from .models import Task

class TaskModelForm(forms.ModelForm):
    class Meta:
        model= Task
        fields='__all__'
        


class TaskDjangoForm(forms.Form):
    taskName=forms.CharField(label="First Name", max_length=100)
    description = forms.CharField(label="Task description", max_length=100)
