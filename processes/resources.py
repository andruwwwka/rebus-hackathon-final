from rest_framework.response import Response
from rest_framework.views import APIView

from camunda.process_definition import comunda_process_definition


class ProcessStartByKeyResource(APIView):

    def post(self, request, key):
        task_result = comunda_process_definition.start_by_key(key, request.data)
        return Response(task_result)


class ProcessStartByIdResource(APIView):

    def post(self, request, id):

        task_result = comunda_process_definition.start_by_id(id, request.data)
        return Response(task_result)
