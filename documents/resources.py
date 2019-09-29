import os
import uuid

# from appy.pod.renderer import Renderer
from django.conf.global_settings import MEDIA_ROOT
from rest_framework.response import Response
from rest_framework.views import APIView
from secretary import Renderer

from rebus.settings import ODT_TEMPLATES_PATH


class GeneratePdfResource(APIView):

    def post(self, request, uid):
        template_file = os.path.join(ODT_TEMPLATES_PATH, 'hunting_ticket.odt')
        result_file = os.path.join(MEDIA_ROOT, f'{str(uuid.uuid4())}.odt')
        # renderer = Renderer(template_file, request.data, result_file)
        # renderer.run()
        engine = Renderer()

        result = engine.render(template_file, **request.data)

        output = open(result_file, 'wb')
        output.write(result)
        return Response({'path': result_file})
