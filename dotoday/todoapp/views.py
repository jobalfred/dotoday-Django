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
