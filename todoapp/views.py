from pyexpat.errors import messages
from django.shortcuts import render, redirect

from todoapp.forms import  TaskModelForm, TaskDjangoForm
from .models import Task

# Create your views here.


#rendering home.html template
def home(request):
    uncompletedTasks = Task.objects.filter(is_completed=False).order_by('-updated_at')

    completedTasks = Task.objects.filter(is_completed=True).order_by('-updated_at')

    context={'uncompletedTasks': uncompletedTasks, 'completedTasks':completedTasks}

    return render(request, 'todoapp/home.html', context )


#rendering addTask.html template
def forms(request):
    modelForm= TaskModelForm()
    djangoForm=TaskDjangoForm()
    context= {
        'modelForm':modelForm, 'djangoForm':djangoForm
    }

    return render(request, 'todoapp/addTask.html', context)

#implementing modelForm
def usingModelForm(request):
    if request.method=='POST':
        modelForms = TaskModelForm(request.POST)
        if modelForms.is_valid():
           modelForms.save()
           return redirect('/')
            
    return redirect('forms')


#implementing djangoForm
def usingDjangoForm(request):
    name= request.POST['taskName']
    describe=request.POST['description']
    Task.objects.create(taskName=name)
    Task.objects.create(description=describe)   
    return redirect('/')

#implementing user created Form            
def usingUserCreatedForm(request):
    task= request.POST['taskName']
    describe= request.POST['description']
    Task.objects.create(taskName=task)
    Task.objects.create(description=describe)
    return redirect('/')

    




    

    