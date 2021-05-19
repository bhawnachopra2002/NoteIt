'''
It contains all the views for 'todo/*' kind of URLs
Each view returns a render request for an html page after processing the request.
All the tests for views are under files of type test_views*.
@login_required mixin is added before each view where login is required for accessing it.
These views are called in urls.py file in todo folder.

'''

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# relative import of forms
from .models import TodoTask
from .forms import AddTaskForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.

''' Add task view is called on add-task url. It renders add_task_view.html file.
An instance of AddTaskForm is passed as context to this html page.
It is tested in test_view_add_task.py file under tests subfolder.
'''

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

''' View all tasks view is called on view-all-tasks url. It renders view_all_tasks.html file.
All tasks beloniging to user is passed as context to this html page.
It is tested in test_view_alltask.py file under tests subfolder in todo.
'''


@login_required
def view_all_tasks(request):
    tasks = (TodoTask.objects.filter(user=request.user))
    return render(request, 'view_all_tasks.html', {'tasks': tasks})

''' Update task view is called on update-task url. It renders update_task.html file.
The updated task with given primary key is passed as context to this html page.
It is tested in test_view_edit_todo.py file under tests subfolder in todo.
'''


@login_required
def update_task(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}
    task = get_object_or_404(TodoTask, id=pk)

    if task.user != request.user:
        messages.error(request, 'You are not authenticated to perform this action')
        return redirect('view-all-tasks')

    # pass the object as instance in form
    form = AddTaskForm(request.POST or None, instance=task)

    # save the data from the form
    if form.is_valid():
        form.save()
        return redirect('view-all-tasks')
    # add form dictionary to context
    context["form"] = form
    return render(request, "update_task.html", context)

''' Confirm Delete task view is called on confirm-delete-task url. It renders confirm_task_delete.html file.
The task with given primary key to be deleted is passed as context to this html page.
It is tested in test_view_confirm_delete.py file under tests subfolder in todo.
'''


@login_required
def confirm_delete_task(request, pk):
    task = get_object_or_404(TodoTask, pk=pk)
    if task.user != request.user:
        messages.error(request, 'You are not authenticated to perform this action')
        return redirect('view-all-tasks')
    context = {
        'task_detail': task,
    }
    return render(request, 'confirm_task_delete.html', context)

''' Delete task view is called on delete-task url. It redirects to view-all-tasks url on successful deletion.
The task with given primary key to be deleted is passed as context to this html page.
It is tested in test_view_delete_task.py file under tests subfolder.
'''

@login_required
def delete_task(request, pk):
    task = get_object_or_404(TodoTask, id=pk)
    if task.user != request.user:
        messages.error(request, 'You are not authenticated to perform this action')
        return redirect('view-all-tasks')
    task.delete()
    messages.success(request, "task deleted successfully")
    return redirect('view-all-tasks')

''' Search task view is called on search-tasks url. It renders search_task.html file.
All tasks beloniging to user containing keyword either in their title or in taggs are passed as context to this html page.
It is tested in test_view_searchtask.py file under tests subfolder.
'''

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
