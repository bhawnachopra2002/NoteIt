from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

''' index view is called on home url. It redirects to view-all-notes url.
It requires user to be logged in.
'''


@login_required
def index(request):
    return redirect('view-all-notes')

''' sign_up view is called on sign-up url. It renders registration/sign_up.html page on successful registration.
It passes an intance of Django's predefined UserCreationForm as a context to this page. On successful login, User 
is redirected to view-all-notes url.
'''

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('view-all-notes')
    context['form'] = form
    return render(request, 'registration/sign_up.html', context)
