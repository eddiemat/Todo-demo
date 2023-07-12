from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404

from todoapp.forms import  TaskModelForm
from .models import Task

# Create your views here.


#rendering home.html template for both uncompleted and completed task
def home(request):
    uncompletedTasks = Task.objects.filter(is_completed=False).order_by('-updated_at')

    completedTasks = Task.objects.filter(is_completed=True).order_by('-updated_at')

    deletedtask= Task.objects.filter(is_deleted=True)

    context={'uncompletedTasks': uncompletedTasks, 'completedTasks':completedTasks, 'deleted': deletedtask}

    return render(request, 'todoapp/home.html', context )


#rendering addTask.html template using two approach "model form" and "djangoform"
def forms(request):
    modelForm= TaskModelForm()
    context= {
        'modelForm':modelForm
    }

    return render(request, 'todoapp/addTask.html', context)

#implementing post of data to database using modelForm
def usingModelForm(request):
    if request.method=='POST':
        modelForms = TaskModelForm(request.POST)
        if modelForms.is_valid():
           modelForms.save()
           return redirect('/')
            
    return redirect('forms')

'''
#implementing post of data to database using djangoForm
def usingDjangoForm(request):
    name= request.POST['taskName']
    describe=request.POST['description']
    Task.objects.create(taskName=name)
    Task.objects.create(description=describe)   
    return redirect('/')

#implementing post of data to database using manual created Form            
def usingUserCreatedForm(request):
    task= request.POST['taskName']
    describe= request.POST['description']
    Task.objects.create(taskName=task)
    Task.objects.create(description=describe)
    return redirect('/')
'''
    
def mark_as_done(request, pk):
    task= get_object_or_404(Task, pk=pk)
    task.is_completed= True
    task.save()
    return redirect('home')


def mark_as_undone(request, pk):
    undone= get_object_or_404(Task, pk=pk)
    undone.is_completed=False
    undone.save()
    return redirect('home') 



def editTaskUsingModelForm(request, pk):

    #object= Task.objects.get(pk=pk)
    object=get_object_or_404(Task, pk=pk)
    formobj= TaskModelForm(instance=object)
    if request.method=="POST":
        formobj= TaskModelForm(request.POST, instance=object)
        if formobj.is_valid():
            formobj.save()
            return redirect('/')

        
    context={'form': formobj, 'task': object}

    return render(request, 'todoapp/edit.html', context)





#implementing edit using djangoForm or user created form
def editTask(request, pk): 
    #get_task= Task.objects.get(pk=pk)
    get_task= get_object_or_404(Task, pk=pk)

    if request.method=='POST':
        editedTaskName= request.POST['taskName']
        editedDescription= request.POST['description']

        get_task.taskName= editedTaskName
        get_task.description=editedDescription

        get_task.save()
        return redirect('/')

    else:

        context={       
          'task': get_task
             }
        return render(request, 'todoapp/editTask.html', context )
    
    
# '''''''' delete tasks and store them into trash ''''''''''''''''

def moveToTrash(request, pk):
    taskToDelete= get_object_or_404(Task, pk=pk)
    return render(request, 'todoapp/confirmMoveToTrash.html', {'taskName':taskToDelete})

def confirmMoveToTrash(request, pk):
    task= get_object_or_404(Task, pk=pk)
    if task:
        task.is_deleted=True
        task.save()
        return redirect('/')

    
def trash(request):
    tasks= Task.objects.filter(is_deleted=True)
    context={'deletedTask': tasks}
    return render(request, 'todoapp/trash.html',context)

# '''''''' permanent delete tasks from trash ''''''''''''''''
   
def confirmPermanentDelete(request, pk):
    taskToDelete=get_object_or_404(Task, pk=pk)
    context={'taskName': taskToDelete }
    return render(request, 'todoapp/confirmPermanentDelete.html', context)
    
def permanentDelete(request, pk):
    taskTodelete= get_object_or_404(Task, pk=pk)
    if taskTodelete:
        taskTodelete.delete()
        return redirect('trash')
    

 # '''''''' restore tasks from trash to home ''''''''''''''''
   
def restore(request, pk):
    taskTorestore= get_object_or_404(Task, pk=pk)
    context={'task': taskTorestore }
    return render(request, 'todoapp/restoreConfirm.html', context)  
    
def restoreConfirm(request,pk):
    taskToRestore= get_object_or_404(Task, pk=pk)
    if taskToRestore:
        taskToRestore.is_deleted=False
        taskToRestore.save()
        return redirect('trash')
    
# '''''''' restore all tasks from trash to home at once''''''''''''''''

def restoreAll(request):
    tasksToRestore=Task.objects.filter(is_deleted=True)
    return render(request, 'todoapp/restoreAllConfirm.html')

def restoreAllConfirm(request):
    deletedTasks=Task.objects.filter(is_deleted=True)
    for i in deletedTasks:
        i.is_deleted=False
        i.save()
    return redirect('trash')


def deleteAllInTrashConfirm(request):
    return render(request, 'todoapp/deleteAllInTrashConfirm.html')

def deleteAllInTrash(request):
    deletedTask=Task.objects.filter(is_deleted=True)
    for task in deletedTask:
        task.delete()
    return redirect('trash')
    
        


