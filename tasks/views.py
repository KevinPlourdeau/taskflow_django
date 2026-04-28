from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")

    total_tasks = tasks.count()
    todo_tasks = tasks.filter(status="todo").count()
    in_progress_tasks = tasks.filter(status="in_progress").count()
    done_tasks = tasks.filter(status="done").count()

    return render(request, "tasks/task_list.html", {
        "tasks": tasks,
        "total_tasks": total_tasks,
        "todo_tasks": todo_tasks,
        "in_progress_tasks": in_progress_tasks,
        "done_tasks": done_tasks,
    })


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    return render(request, "tasks/task_create.html", {
        "form": form
    })

def task_update(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/task_update.html", {
        "form": form,
        "task": task
    })

def task_delete(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    return render(request, "tasks/task_delete.html", {
        "task": task
    })