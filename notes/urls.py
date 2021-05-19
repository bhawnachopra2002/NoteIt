# from django.contrib import admin
from django.urls import path
from . import views

'''url patterns for various views are defined. The first argument contains followup url in addition to base url.
Here base url is /notes/ . The second argument defines the functions to be called while fetching these urls. 
Third argument is name assigned to the url and it can be called by reverse function

-> add/ : It directs to the view where user can add new notes.
-> view_all/ : It directs to the view where user can see all the notes(in brief).
-> view/<id> : It directs to the view where user can see a particular note in detail.
-> update/<id> : It directs to the view where user can update existing notes.
-> confirm_delete/<id> : It directs to the view where confirm_Delete dialog box is displayed.
-> delete/<id> : It directs to view where delete functionality is performed.
-> search : It directs to the view where user can see all the notes(in brief) containing keyword in either their title or tags.

'''

urlpatterns = [
    path('add/', views.add_note_view, name="add-note"),
    path('view_all/', views.view_all_notes, name="view-all-notes"),
    path('view/<int:pk>', views.view_note, name='view-note'),
    path('update/<int:pk>', views.update_note, name='update-note'),
    path('confirm_delete/<int:pk>', views.confirm_delete_note, name='confirm-delete-note'),
    path('delete/<int:pk>', views.delete_note, name='delete-note'),
    path('search/', views.search_note, name='search-notes'),
]
