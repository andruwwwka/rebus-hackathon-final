from django.urls import path

from tasks.resources import TaskResource, TaskFormResource

app_name = "tasks"

urlpatterns = [
    path('', TaskResource.as_view()),
    path(r'form/<slug:id>', TaskFormResource.as_view()),
]