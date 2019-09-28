from django.urls import path

from tasks.resources import TaskResources

app_name = "tasks"

urlpatterns = [
    path('', TaskResources.as_view()),
]