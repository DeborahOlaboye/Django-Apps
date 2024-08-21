from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasklist', views.task_lists, name='tasks'),
    path('createtask', views.create_task, name = 'create_task'),
    path('updatetask/<int:task_id>/', views.update_task, name = 'update_task'),
    path('deletetask/<int:task_id>/', views.delete_task, name = 'delete_task'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]