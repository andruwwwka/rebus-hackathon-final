import requests

from camunda.base import CamundaWrapper, CamundaBadRequest, CamundaNotFound


class ComundaDeployment(CamundaWrapper):

    def __init__(self):
        super(ComundaDeployment, self).__init__()
        self.server += '/deployment'

    def list(self):
        # GET /deployment
        response = requests.get(self.server)
        if response.status_code != 200:
            raise CamundaBadRequest()
        return response.json()

    def create(self, data):
        # POST /deployment/create
        response = requests.post(f'{self.server}/create', data=data)
        if response.status_code != 200:
            raise CamundaBadRequest()
        return response.json()

    def resources_data(self, id, resource_id):
        # GET /deployment/{id}/resources/{resourceId}/data
        response = requests.get(self.server)
        if response.status_code != 200:
            raise CamundaNotFound()
        return response.json()

    def delete(self, id):
        # DELETE /deployment/{id}
        response = requests.delete(f'{self.server}/{id}')
        if response.status_code != 204:
            raise CamundaNotFound()
        return True


camunda_deployment = ComundaDeployment()
