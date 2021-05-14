# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # below path uses index view as home of this app
    path('add/', views.add_note_view, name="add-note"),
    path('view_all/', views.view_all_notes, name="view-all-notes"),
    path('view/<int:pk>', views.view_note, name='view-note'),
    path('update/<int:pk>', views.update_note, name='update-note'),
    path('confirm_delete/<int:pk>', views.confirm_delete_note, name='confirm-delete-note'),
    path('delete/<int:pk>', views.delete_note, name='delete-note'),
    path('search/', views.search_note, name='search-notes'),
]
