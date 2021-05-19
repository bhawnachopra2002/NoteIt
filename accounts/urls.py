# from django.contrib import admin
from django.urls import path
from . import views

'''url patterns for various views are defined. 
The first argument contains url. The second argument defines the functions to be called while fetching these urls. 
Third argument is name assigned to the url and it can be called by reverse function

-> '' : It directs to the view where user is redirected to view-all-notes page after logging in.
-> accounts/sign_up/ : It directs to the view for sign_up page.

'''

urlpatterns = [
    path('', views.index, name="home"),
    path('accounts/sign_up/', views.sign_up, name="sign-up"),
]
