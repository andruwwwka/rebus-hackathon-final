from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from camunda.deployment import camunda_deployment
from core.decorators import with_serializer
from process_management.serializers import ProcessManagementCreateRequestSerializer


class ProcessManagementCreateResource(APIView):

    @with_serializer(ProcessManagementCreateRequestSerializer, success_code=status.HTTP_200_OK)
    def post(self, request, serializer):
        process = camunda_deployment.create(serializer.validated_data)
        return Response(process)


class ProcessManagementSchemaDataResource(APIView):

    def get(self, request, id, resource_id):
        schema = camunda_deployment.resources_data(id, resource_id)
        return (schema)


class ProcessManagementDeleteResource(APIView):

    def delete(self, request, id):
        camunda_deployment.delete(id)
        return Response('Ok')


class ProcessManagementListResource(APIView):

    def get(self, request):
        processes = camunda_deployment.list()
        return Response(processes)
