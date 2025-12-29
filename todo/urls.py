from django.urls import path
from .views import (
    AllTaskView, 
    TaskDetailsView, 
    AddTaskView, 
    SearchTaskView, 
    UpdateTaskView, 
    DeleteTaskView
)

app_name = 'todo'
urlpatterns = [
    path('my_tasks/', AllTaskView.as_view(), name='tasks'),
    path('task_details/<slug:slug>/', TaskDetailsView.as_view(), name='task_details'),
    path('search_task/', SearchTaskView.as_view(), name='search_task'),
    path('add_task/', AddTaskView.as_view(), name='add_task'),
    path('update_task/<int:id>/', UpdateTaskView.as_view(), name='update_task'),
    path('delete_task/<int:id>/', DeleteTaskView.as_view(), name='delete_task')
]
