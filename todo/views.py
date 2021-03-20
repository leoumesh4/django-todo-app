from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo


def home(request):
    tasks = Todo.objects.all()
    return render(request, 'todo/to_do_list.html', {'tasks': tasks})


def delete(request, pk):
    tasks = Todo.objects.get(id=pk)
    tasks.delete()
    return redirect('/')


def insert(request):
    if request.method == "POST":
        tasks = request.POST.get('tasks')
        todo = Todo(content=request.POST.get('tasks'))
        todo.save()
    tasks = Todo.objects.all()
    return render(request, 'todo/to_do_list.html', {'tasks': tasks})


