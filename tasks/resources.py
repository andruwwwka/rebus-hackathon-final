from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from camunda.task import comunda_task
from tasks.serializers import TaskResponseSerializer


class TaskResources(APIView):

    def get(self, request):
        tasks = comunda_task.list()
        return Response(tasks)

# список
# пофильтровать по асигнеру
# завершить