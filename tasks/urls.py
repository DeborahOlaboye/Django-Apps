from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasklist', views.task_lists, name='tasks'),
    path('createtask', views.create_task, name = 'Create Task'),
    path('updatetask/<int:task_id>/', views.update_task, name = 'Update Task'),
    path('deletetask/<int:task_id>/', views.delete_task, name = 'Delete Task'),
    path('register/', views.register, name='register'),
]