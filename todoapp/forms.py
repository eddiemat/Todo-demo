from django import forms
from .models import Task

class TaskModelForm(forms.ModelForm):
    class Meta:
        model= Task
        fields=['taskName', 'description']
        labels= {'taskName': 'Enter Task Name:', 'description':'Describe your Task' }
        

'''
class TaskDjangoForm(forms.Form):
    taskName=forms.CharField(label="First Name", max_length=100 )
    description = forms.CharField(label="Task description", max_length=100)
'''