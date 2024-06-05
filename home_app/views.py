from django.shortcuts import render,redirect
from .models import Todo
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import TodoCreateForm, TodoUpdateForm
from django.views import View
from django.views.generic import ListView
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'home_app/home.html', {'todos': todos})

def base(request):
    return render(request, 'home_app/base.html', {})


def todo_detail_view(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'home_app/detail.html', context={'todo': todo})

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'todo delete succfuly', extra_tags='success')
    return  redirect('/')

def create_form(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data
            Todo.objects.create(title=x['title'], body=x['body'], created=x['created'])
            
            messages.success(request, 'todo create success', extra_tags='success')
            return redirect('home_app:home')
           
    else:
        form = TodoCreateForm()
    return render(request, 'home_app/create.html', context={'form': form})
    


def update_todo(request,  todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'your todo update succesfuly', extra_tags='success')
            return redirect('home_app:detail_todos', todo_id)
        
    
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'home_app/update.html', context={'form': form})
        
        
        
