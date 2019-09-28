from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from camunda.process_definition import comunda_process_definition
from core.decorators import with_serializer
from processes.serializers import ProcessStartRequestSerializer


class ProcessStartByKeyResource(APIView):

    # @with_serializer(ProcessStartRequestSerializer, success_code=status.HTTP_200_OK)
    def post(self, request, key):
        task_result = comunda_process_definition.start_by_key(key, request.data)
        return Response(task_result)


class ProcessStartByIdResource(APIView):

    # @with_serializer(ProcessStartRequestSerializer, success_code=status.HTTP_200_OK)
    # def post(self, request, id, serializer):
    def post(self, request, id):

        task_result = comunda_process_definition.start_by_id(id, request.data)
        return Response(task_result)
