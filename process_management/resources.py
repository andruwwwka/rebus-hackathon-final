from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from camunda.deployment import camunda_deployment


class ProcessManagementCreateResource(APIView):

    def post(self, request):
        data = request.data.copy()
        files = data.pop('files')
        process = camunda_deployment.create(data, files)
        return Response(process)


class ProcessManagementSchemaDataResource(APIView):

    def get(self, request, id, resource_id):
        schema = camunda_deployment.resources_data(id, resource_id)
        response = HttpResponse(schema, content_type='text/xml')
        response['Content-Disposition'] = f'attachment; filename="{resource_id}.bpmn"'
        return response


class ProcessManagementDeleteResource(APIView):

    def delete(self, request, id):
        camunda_deployment.delete(id)
        return Response('Ok')


class ProcessManagementListResource(APIView):

    def get(self, request):
        processes = camunda_deployment.list()
        return Response(processes)


class ProcessManagementSchemaListResource(APIView):

    def get(self, request, id):
        schema = camunda_deployment.resources_list(id)
        return Response(schema)
