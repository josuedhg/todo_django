from django.urls import path

from .views import ListTasks, CreateTask, RetrieveUpdateDestroyTask

urlpatterns = [
    # Task api
    path('api/v1/task/list', ListTasks.as_view(), name='list_tasks'),
    path('api/v1/task/create', CreateTask.as_view(), name='create_task'),
    path('api/v1/task/<int:pk>', RetrieveUpdateDestroyTask.as_view(),
         name='retrieve_update_destroy_task'),
]
