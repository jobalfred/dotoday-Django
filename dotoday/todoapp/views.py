from django.shortcuts import render, redirect
from .models import TaskToDo
from .forms import ToDoFroms


# Create your views here.
def home(request):
    tasks = TaskToDo.objects.all()
    form = ToDoFroms()
    if request.method == 'POST':
        form = ToDoFroms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks':tasks,'form':form}
    return render(request,'home.html', context)

def updateTask(request, pk):
    task = TaskToDo.objects.get(id=pk)
    form = ToDoFroms(instance=task)
    if request.method == 'POST':
        form = ToDoFroms(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'update.html', context)


def deleteTask(request, pk):
    task = TaskToDo.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete_task.html', {'task':task})
