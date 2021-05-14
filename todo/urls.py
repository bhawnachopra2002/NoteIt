from django.urls import path
from . import views

urlpatterns = [
    # below path uses index view as home of this app
    path('add/', views.add_task_view, name="add-task"),
    path('view_all/', views.view_all_tasks, name="view-all-tasks"),
    path('update/<int:pk>', views.update_task, name='update-task'),
    path('confirm_delete/<int:pk>', views.confirm_delete_task, name='confirm-delete-task'),
    path('delete/<int:pk>', views.delete_task, name='delete-task'),
    path('search/', views.search_todos, name='search-tasks'),
]
