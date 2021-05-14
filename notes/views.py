from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# relative import of forms
from .models import Note
from .forms import AddNoteForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.


@login_required
def add_note_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = AddNoteForm(request.POST or None)
    if form.is_valid():
        note = form.save(commit=False)
        note.user = request.user
        note.save()
        form.save_m2m()
        messages.success(request, "Note added successfully")
        return redirect('view-all-notes')
    context['form'] = form
    return render(request, "add_note_view.html", context)


@login_required
def view_all_notes(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'view_all_notes.html', {'notes': notes})


@login_required
def view_note(request, pk):
    note = Note.objects.get(id=pk)
    if note.user != request.user:
        messages.error(request, 'You are not authenticated to perform this action')
        return redirect('view-all-notes')
    return render(request, 'view_note.html', {'note': note})


# update view for details
@login_required
def update_note(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    note = get_object_or_404(Note, id=pk)

    if note.user != request.user:
        messages.error(request, 'You are not authenticated to perform this action')
        return redirect('view-all-notes')

    # pass the object as instance in form
    form = AddNoteForm(request.POST or None, instance=note)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('view-note', pk=pk)
    # add form dictionary to context
    context["form"] = form
    return render(request, "update_note.html", context)


@login_required
def confirm_delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if note.user != request.user:
        messages.error(request, 'You are not authenticated to perform this action')
        return redirect('view-all-notes')
    # note.delete()
    context = {
        'note_detail': note,
    }
    return render(request, 'confirm_note_delete.html', context)


@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, id=pk)
    if note.user != request.user:
        messages.error(request, 'You are not authenticated to perform this action')
        return redirect('view-all-notes')
    note.delete()
    messages.success(request, "Note deleted successfully")
    return redirect('view-all-notes')


@login_required
def search_note(request):
    keyword = request.GET.get('search')
    if keyword:
        searchednotes = Note.objects.filter(Q(user=request.user) & ((Q(title__icontains=keyword) | Q(tags__name__icontains=keyword)))).distinct()
        if(searchednotes):
            return render(request, "search_note.html", {'notes': searchednotes})
        else:
            return render(request, "search_note.html", None)
    else:
        return redirect('view-all-notes')
