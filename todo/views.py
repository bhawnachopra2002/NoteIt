from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# relative import of forms
from .models import TodoTask
from .forms import AddTaskForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.


@login_required
def add_task_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = AddTaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        form.save_m2m()
        messages.success(request, "Task added successfully")
        return redirect('view-all-tasks')
    context['form'] = form
    return render(request, "add_task_view.html", context)


@login_required
def view_all_tasks(request):
    tasks = (TodoTask.objects.filter(user=request.user))
    return render(request, 'view_all_tasks.html', {'tasks': tasks})


# update view for details
@login_required
def update_task(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    task = get_object_or_404(TodoTask, id=pk)

    if task.user != request.user:
        messages.error(request, 'You are not authenticated to perform this action')
        return redirect('view-all-tasks')

    # pass the object as instance in form
    form = AddTaskForm(request.POST or None, instance=task)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('view-all-tasks')
    # add form dictionary to context
    context["form"] = form
    return render(request, "update_task.html", context)


@login_required
def confirm_delete_task(request, pk):
    task = get_object_or_404(TodoTask, pk=pk)
    if task.user != request.user:
        messages.error(request, 'You are not authenticated to perform this action')
        return redirect('view-all-tasks')
    # note.delete()
    context = {
        'task_detail': task,
    }
    return render(request, 'confirm_task_delete.html', context)


@login_required
def delete_task(request, pk):
    task = get_object_or_404(TodoTask, id=pk)
    if task.user != request.user:
        messages.error(request, 'You are not authenticated to perform this action')
        return redirect('view-all-tasks')
    task.delete()
    messages.success(request, "task deleted successfully")
    return redirect('view-all-tasks')


@login_required
def search_todos(request):
    keyword = request.GET.get('search')
    if keyword:
        searchedtask = TodoTask.objects.filter(Q(user=request.user) & ((Q(title__icontains=keyword) | Q(tags__name__icontains=keyword)))).distinct()
        if(searchedtask):
            return render(request, "search_task.html", {'tasks': searchedtask})
        else:
            return render(request, "search_task.html", None)
    else:
        return redirect('view-all-tasks')
