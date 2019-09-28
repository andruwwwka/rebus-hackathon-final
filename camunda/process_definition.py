import requests

from camunda.base import CamundaWrapper, CamundaBadRequest


class ComundaProcessDefinition(CamundaWrapper):

    def __init__(self):
        super(ComundaProcessDefinition, self).__init__()
        self.server += '/process-definition'

    def start_by_id(self, id, body):
        # POST /process-definition/{id}/start

        response = requests.post(f'{self.server}/{id}/start', json=body, verify=False, headers=self.header)
        if response.status_code != 200:
            raise CamundaBadRequest()
        return response.json()

    def start_by_key(self, key, body):
        # POST /process-definition/key/{key}/start
        response = requests.post(f'{self.server}/key/{key}/start', json=body, verify=False, headers=self.header)
        if response.status_code != 200:
            raise CamundaBadRequest()
        return response.json()


comunda_process_definition = ComundaProcessDefinition()
