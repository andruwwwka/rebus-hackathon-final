from django.urls import path

from tasks.resources import TaskResource, TaskFormResource, TaskCompleteResource

app_name = "tasks"

urlpatterns = [
    path('', TaskResource.as_view()),
    path(r'form/<slug:id>', TaskFormResource.as_view()),
    path(r'<slug:id>/complete', TaskCompleteResource.as_view()),
]