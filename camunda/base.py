from django.conf import settings


class CamundaNotFound(BaseException):
    pass


class CamundaBadRequest(BaseException):
    pass


class CamundaWrapper:
    def __init__(self):
        self.server = settings.CAMUNDA_URL