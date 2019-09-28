from django.urls import path

from process_management.resources import ProcessManagementListResource, ProcessManagementCreateResource, \
    ProcessManagementDeleteResource, ProcessManagementSchemaDataResource, ProcessManagementSchemaListResource

urlpatterns = [
    path('', ProcessManagementListResource.as_view()),
    path('create', ProcessManagementCreateResource.as_view()),
    path(r'<slug:id>/schema_list', ProcessManagementSchemaListResource.as_view()),
    path(r'<slug:id>/schema/<slug:resource_id>', ProcessManagementSchemaDataResource.as_view()),
    path(r'delete/<slug:id>', ProcessManagementDeleteResource.as_view()),
]
