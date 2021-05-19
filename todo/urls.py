from django.urls import path
from . import views

'''url patterns for various views are defined. The first argument contains followup url in addition to base url.
Here base url is /todo/ . The second argument defines the functions to be called while fetching these urls. 
Third argument is name assigned to the url and it can be called by reverse function

-> add/ : It directs to the view where user can add new tasks.
-> view_all/ : It directs to the view where user can see all the tasks(in brief).
-> update/<id> : It directs to the view where user can update existing tasks.
-> confirm_delete/<id> : It directs to the view where confirm_Delete dialog box is displayed.
-> delete/<id> : It directs to view where delete functionality is performed. 
-> search/ : It directs to the view where user can see all the tasks(in brief) containing keyword in either their title or tags.

'''


urlpatterns = [
    # below path uses index view as home of this app
    path('add/', views.add_task_view, name="add-task"),
    path('view_all/', views.view_all_tasks, name="view-all-tasks"),
    path('update/<int:pk>', views.update_task, name='update-task'),
    path('confirm_delete/<int:pk>', views.confirm_delete_task, name='confirm-delete-task'),
    path('delete/<int:pk>', views.delete_task, name='delete-task'),
    path('search/', views.search_todos, name='search-tasks'),
]
