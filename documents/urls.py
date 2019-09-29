from django.urls import path

from documents.resources import GeneratePdfResource


urlpatterns = [
    path(r'<slug:uid>/generate/', GeneratePdfResource.as_view()),
]
