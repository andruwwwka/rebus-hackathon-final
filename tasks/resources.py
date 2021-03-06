from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from camunda.task import comunda_task
from core.decorators import with_serializer
from tasks.serializers import TaskListGetParametersSerializer


class TaskResource(APIView):

    @with_serializer(TaskListGetParametersSerializer, success_code=status.HTTP_200_OK,
                     dataGetter=lambda request: request.GET)
    def get(self, request, serializer):
        tasks = comunda_task.list(serializer.validated_data)
        return Response(tasks)


class TaskFormResource(APIView):

    def get(self, request, id):
        form = comunda_task.form_key(id)
        return Response(form)


class TaskCompleteResource(APIView):

    def post(self, request, id):
        comunda_task.complete(id, request.data)
        return Response('Ok')
