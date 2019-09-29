from django.urls import path

from processes.resources import ProcessStartByKeyResource, ProcessStartByIdResource


urlpatterns = [
    path(r'key/<slug:key>/start/', ProcessStartByKeyResource.as_view()),
    path(r'id/<slug:id>/start/', ProcessStartByIdResource.as_view()),
]
