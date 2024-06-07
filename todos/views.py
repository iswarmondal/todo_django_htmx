from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
    return redirect('todo_list')

def toggle_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    if 'HX-Request' in request.headers:
        return render(request, 'todos/_todo_item.html', {'todo': todo})
    
    return redirect('todo_list') 
