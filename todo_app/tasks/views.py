from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from .models import Task
from .forms import TaskForm
from .forms import ConfirmDeleteForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, "index.html",{})

@login_required
def task_lists(request):
    if request.user.is_superuser:
        tasks = Task.objects.all().order_by("-created")
    # Handles the display of tasks to the logged-in user.
    # The user will only see tasks that are either assigned to them or created by them.
    else:
        tasks = Task.objects.filter(assigned_to=request.user).order_by("-created")
    return render(request, "task_list.html", {"tasks": tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Create a new Task object from the form data without saving it to the database yet
            task = form.save(commit=False)
            # Set the `created_by` field of the task to the current user
            task.created_by = request.user
            task.save()
            #The reverse function is used to resolve the URL name 'tasks' into its corresponding URL path.
            return HttpResponseRedirect(reverse('tasks'))
    else:
        form = TaskForm()
    return render(request, "create_task.html", {"form": form})

def update_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_update.html', {"form": form})
        
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = ConfirmDeleteForm(request.POST)
        if form.is_valid():
            task.delete()
            return redirect('tasks')
    else:
        form = ConfirmDeleteForm()
    return render(request, 'confirm_delete.html', {"form": form})
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        else:
            print(form.errors)
    else:
        form=UserCreationForm
    return render(request, 'registration/register.html', {"form": form})