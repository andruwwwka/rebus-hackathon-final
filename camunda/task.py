import requests

from camunda.base import CamundaWrapper, CamundaBadRequest


class ComundaTask(CamundaWrapper):

    def __init__(self):
        super(ComundaTask, self).__init__()
        self.server += '/task'

    def list(self, query):
        # GET /task
        response = requests.get(self.server, params=query)
        if response.status_code != 200:
            raise CamundaBadRequest()
        return response.json()

    def form_key(self, id):
        # GET /task/{id}/form
        response = requests.get(f'{self.server}/{id}/form')
        if response.status_code != 200:
            raise CamundaBadRequest()
        return response.json()

    def complete(self, id, body):
        # POST /task/{id}/complete
        response = requests.post(f'{self.server}/{id}/complete', body=body)
        if response.status_code != 204:
            raise CamundaBadRequest()
        return True


comunda_task = ComundaTask()
